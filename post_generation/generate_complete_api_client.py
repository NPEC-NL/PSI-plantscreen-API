# coding: utf-8
"""
Script to generate a Python class with all wrapped calls
from OpenAPI client APIs.
"""
import sys
import importlib
import inspect
import os
import re
import typing
import plantscreen.models as models_module


OUTPUT_FILE = "plantscreen/complete_api_client.py"

# Requires plantscreen to be installed with pip!
#  pip install .
# Only wraps around the functions themselves.
# Not the *_with_http_info and *_without_preload_content


def add_to_init():
    # --- Add CompleteAPIClient to __init__.py ---
    init_path = os.path.join(os.path.dirname(OUTPUT_FILE), "__init__.py")
    with open(init_path, "r", encoding="utf-8") as f:
        init_lines = f.readlines()
    # Add import if not present
    import_line = (
        "from plantscreen.complete_api_client import CompleteAPIClient\n"
    )
    if not any(
        "CompleteAPIClient" in line and "import" in line
        for line in init_lines
    ):
        # Find first non-comment, non-docstring line after imports
        insert_at = 0
        for i, line in enumerate(init_lines):
            if (
                line.strip().startswith("from")
                or line.strip().startswith("import")
            ):
                insert_at = i + 1
        init_lines.insert(insert_at, import_line)
    # Add to __all__ if not present
    for i, line in enumerate(init_lines):
        if line.strip().startswith("__all__"):
            # Find the closing bracket
            for j in range(i, len(init_lines)):
                if "]" in init_lines[j]:
                    if '"CompleteAPIClient"' not in ''.join(init_lines[i:j+1]):
                        # Insert before closing bracket
                        init_lines.insert(j, '    "CompleteAPIClient",\n')
                    break
            break
    with open(init_path, "w", encoding="utf-8") as f:
        f.writelines(init_lines)
    print(
        f"Generated API client written to {OUTPUT_FILE} and added to __init__.py"
    )


def get_json_field_from_return_type(api_module, return_type):
    # Helper to get the json_* field from the return type
    if return_type is inspect._empty:
        return None, False
    # If it's a string annotation, resolve it
    if isinstance(return_type, str):
        try:
            return_type = eval(return_type, api_module.__dict__)
        except Exception:
            return None, False
    # Prefer model_fields (Pydantic v2+), fallback to __fields__ (v1)
    if hasattr(return_type, 'model_fields'):
        fields = getattr(return_type, 'model_fields')
        if isinstance(fields, dict) and fields:
            return list(fields.keys())[0], False
    elif hasattr(return_type, '__fields__'):
        fields = getattr(return_type, '__fields__')
        if isinstance(fields, dict) and fields:
            return list(fields.keys())[0], False
    # Try __annotations__
    if hasattr(return_type, '__annotations__'):
        ann = return_type.__annotations__
        if ann:
            return list(ann.keys())[0], False
    return None, False


def extract_base_type(ann):
    """Extract the base type from a typing.Annotated type.
    For example, if ann is Annotated[int, SomeMetadata], this will return int.
    If ann is not an Annotated type, it will return ann unchanged.
    """
    if typing.get_origin(ann) is typing.Annotated:
        return typing.get_args(ann)[0]
    return ann


def clean_optional(type_str):
    # Remove nested Optional[Optional[X]] and Optional[X], output just X
    inner = re.sub(
        r'Optional\[([^\]]+)\]', r'\1', type_str
    )
    return re.sub(
        r'Optional\[Optional\[([^\]]+)\]\]', r'\1', inner
    )


def unwrap_type(t):
    """Unwrap complex types to get a more readable type hint string.
    This handles Union, List, Dict, Tuple, and also maps custom types to
    standard types for better readability in the generated code.
    """
    # Map custom types to standard types
    custom_type_map = {
        'StrictInt': 'int',
        'StrictStr': 'str',
        'StrictFloat': 'float',
        'StrictBool': 'bool',
        'StrictBytes': 'bytes',
        'StrictDate': 'datetime',
        'StrictDatetime': 'datetime',
        'Field': '',  # ignore Field
        'NoneType': 'None',
        'Any': 'Any',
    }
    t = extract_base_type(t)
    # Handle Union, remove NoneType and Annotated
    if getattr(t, '__origin__', None) is typing.Union:
        union_types = [
            unwrap_type(tt)
            for tt in t.__args__
            if unwrap_type(tt) not in ('Annotated', 'NoneType', 'None')
        ]
        if 'None' in [unwrap_type(tt) for tt in t.__args__]:
            if len(union_types) == 1:
                return f'Optional[{union_types[0]}]'
            return f"Optional[Union[{', '.join(union_types)}]]"
        return f"Union[{', '.join(union_types)}]"
    if getattr(t, '__origin__', None) is list or getattr(t, '__origin__', None) is typing.List:
        elem_type = unwrap_type(t.__args__[0])
        return f'List[{elem_type}]'
    if getattr(t, '__origin__', None) is dict or getattr(t, '__origin__', None) is typing.Dict:
        key_type = unwrap_type(t.__args__[0])
        val_type = unwrap_type(t.__args__[1])
        return f'Dict[{key_type}, {val_type}]'
    if getattr(t, '__origin__', None) is tuple or getattr(t, '__origin__', None) is typing.Tuple:
        tuple_types = [unwrap_type(tt) for tt in t.__args__]
        return f"Tuple[{', '.join(tuple_types)}]"
    if hasattr(t, '__name__'):
        name = t.__name__
        return custom_type_map.get(name, name)
    t_str = str(t)
    for k, v in custom_type_map.items():
        if k in t_str:
            t_str = t_str.replace(k, v)
    # Remove Annotated remnants
    t_str = t_str.replace('Annotated', '').replace('NoneType', 'None')
    return t_str.strip(', ').replace(' ,', ',')


def generate_combined_api_client():
    # --- Generate the combined API client class ---

    # Dynamically import the API package
    api_module = importlib.import_module("plantscreen.api")

    # Add model class attributes (not starting with 'Json')
    model_names = [
        name
        for name in dir(models_module)
        if name[0].isupper() and not name.startswith('Json')
    ]

    class_lines = [
        "# coding: utf-8",
        '"""',
        'Auto-generated API client wrapper with direct methods for all endpoints.',
        '"""',
        'from plantscreen.api_client import ApiClient',
        'import plantscreen.api as api_module',
        'from typing import Any, Optional, Union, Tuple, List, Dict',
        'from datetime import datetime',
        (
            "from plantscreen.models import "
            f"{', '.join(sorted(model_names))}"
        ),
        '\n',
        '',
        'class CompleteAPIClient(ApiClient):',
        '    def __init__(self, *args: Any, **kwargs: Any) -> None:',
        '        super().__init__(*args, **kwargs)',
    ]

    # Find all API classes
    api_classes = [
        getattr(api_module, name)
        for name in dir(api_module)
        if name.endswith('Api') and name[0].isupper()
    ]
    for api_cls in api_classes:
        class_lines.append(
            f'        self._{api_cls.__name__}: api_module.{api_cls.__name__} = '
            f'api_module.{api_cls.__name__}(self)'
        )
    class_lines.append('')

    # For each API class, add its public methods to the wrapper
    for api_cls in api_classes:
        for name, method in inspect.getmembers(api_cls, predicate=inspect.isfunction):
            if (
                name.startswith('_') or name == '__init__' or
                name.endswith('_with_http_info') or name.endswith('_without_preload_content')
            ):
                continue
            sig = inspect.signature(method)
            params = [p for p in sig.parameters.values() if p.name != 'self']
            param_defs = []
            call_args = []

            for p in params:
                param_type = 'Any'
                ann = p.annotation
                if ann is not inspect._empty:
                    param_type = unwrap_type(ann)
                else:
                    # Try to infer from docstring
                    doc = method.__doc__ or ''
                    import re
                    doc_match = re.search(rf'{p.name}\s*\(([^)]+)\)', doc)
                    if doc_match:
                        doc_type = doc_match.group(1).strip()
                        doc_type_map = {
                            'integer': 'int',
                            'string': 'str',
                            'boolean': 'bool',
                            'float': 'float',
                            'datetime': 'datetime',
                            'date': 'datetime',
                        }
                        param_type = doc_type_map.get(
                            doc_type.lower(), doc_type
                        )
                    elif p.default is not inspect._empty:
                        if isinstance(p.default, int):
                            param_type = 'int'
                        elif isinstance(p.default, str):
                            param_type = 'str'
                        elif isinstance(p.default, bool):
                            param_type = 'bool'
                        elif isinstance(p.default, float):
                            param_type = 'float'
                        elif (
                            hasattr(p.default, '__class__')
                            and p.default.__class__.__name__ == 'datetime'
                        ):
                            param_type = 'datetime'
                if p.default is not inspect._empty:
                    param_defs.append(
                        f"{p.name}: {param_type} = {repr(p.default)}"
                    )
                else:
                    param_defs.append(f"{p.name}: {param_type}")
                call_args.append(p.name)
            params_str = ', '.join(param_defs)
            call_args_str = ', '.join(call_args)
            # Dynamically determine the correct json_* attribute
            return_type = sig.return_annotation
            json_field, is_api_response = get_json_field_from_return_type(
                sys.modules[api_cls.__module__], return_type
            )
            # Determine return type hint, unwrap generics and Annotated
            if return_type is not inspect._empty:
                return_type_hint = unwrap_type(return_type)
            else:
                return_type_hint = 'Any'
            # If the wrapper returns a field from the result
            # use the field's type if possible
            field_type_hint = None
            if (
                json_field
                and hasattr(return_type, '__annotations__')
                and json_field in return_type.__annotations__
            ):
                field_type_hint = unwrap_type(
                    return_type.__annotations__[json_field]
                )
            if json_field:
                # Use the field's type if available, otherwise fallback to Any
                hint = field_type_hint if field_type_hint else 'Any'
                # Remove redundant Optional wrapping
                hint_clean = clean_optional(hint)
                if params_str:
                    class_lines.append(
                        f'    def {name}(self, {params_str}) -> {hint_clean}:'
                    )
                    class_lines.append(
                        f'        result = self._{api_cls.__name__}.{name}('
                        f'{call_args_str})'
                    )
                    class_lines.append(
                        f'        return getattr(result, "{json_field}", None)'
                    )
                else:
                    class_lines.append(f'    def {name}(self) -> {hint_clean}:')
                    class_lines.append(f'        result = self._{api_cls.__name__}.{name}()')
                    class_lines.append(f'        return getattr(result, "{json_field}", None)')
            else:
                if params_str:
                    class_lines.append(f'    def {name}(self, {params_str}) -> {return_type_hint}:')
                    class_lines.append(f'        return self._{api_cls.__name__}.{name}({call_args_str})')
                else:
                    class_lines.append(f'    def {name}(self) -> {return_type_hint}:')
                    class_lines.append(f'        return self._{api_cls.__name__}.{name}()')
            class_lines.append('')

    # Write to output file
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(class_lines))


generate_combined_api_client()
add_to_init()
