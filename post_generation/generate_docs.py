# Script to generate docs/CompleteAPIClient.md for mkdocs
import ast
from pathlib import Path
import re


def _extract_signature_and_doc(node, skip_first_arg=False):
    """
    Helper to extract signature, docstring, and return type from
    a FunctionDef node."""
    args = []
    arg_nodes = node.args.args[1:] if skip_first_arg else node.args.args
    for arg in arg_nodes:
        arg_str = arg.arg
        if arg.annotation:
            arg_str += ': ' + ast.unparse(arg.annotation)
        args.append(arg_str)
    # Handle defaults
    num_defaults = len(node.args.defaults)
    num_args = len(arg_nodes)
    defaults = [None] * (num_args - num_defaults) + node.args.defaults
    sig_args = []
    for i, arg in enumerate(args):
        default = defaults[i] if i < len(defaults) else None
        if default is not None:
            try:
                default_val = ast.literal_eval(default)
                arg += f'={repr(default_val)}'
            except Exception:
                arg += '=...'
        sig_args.append(arg)
    signature = f"{node.name}({', '.join(sig_args)})"
    docstring = ast.get_docstring(node) or ''
    returns = ast.unparse(node.returns) if node.returns else ''
    return {
        'name': node.name,
        'signature': signature,
        'docstring': docstring,
        'returns': returns,
    }


def extract_methods_from_class(source, class_name):
    """
    Extract all public methods, their signatures,
    docstrings, and return types from a class in the given source code."""
    tree = ast.parse(source)
    methods = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.ClassDef)
            and node.name == class_name
        ):
            for item in node.body:
                if (
                    isinstance(item, ast.FunctionDef)
                    and not item.name.startswith('_')
                ):
                    methods.append(
                        _extract_signature_and_doc(item, skip_first_arg=True)
                    )
    return methods


def extract_methods_from_source(source):
    """Extract all top-level (loose) functions from the given source code."""
    tree = ast.parse(source)
    methods = []
    for node in tree.body:
        if (
            isinstance(node, ast.FunctionDef)
            and not node.name.startswith('_')
        ):
            methods.append(
                _extract_signature_and_doc(node, skip_first_arg=False)
            )
    return methods


def linkify_return_type(ret_type: str, model_docs: dict) -> str:
    """
    Convert a return type into a Markdown link if it corresponds to a known model.
    Args:
        ret_type (str): The return type to linkify
        model_docs (dict): A mapping from model names to documentation links
    Returns:
        str: The linkified return type
    """
    # Handle List[Model], Union[Model, ...], Model, etc.
    if not ret_type:
        return ''
    # Remove typing wrappers for mapping
    base = ret_type
    # Handle List[...] and Union[...]
    m = re.match(r'(?:List|Sequence)\[(\w+)\]', base)
    if m:
        model = m.group(1)
        link = model_docs.get(model, None)
        if link:
            return (
                f'List[[{model}]({link})]'
            )
    m = re.match(r'(?:Optional\[)?(\w+)(?:\])?', base)
    if m:
        model = m.group(1)
        link = model_docs.get(model, None)
        if link:
            return (
                f'[{model}]({link})'
            )
    # Fallback: just return the type
    return ret_type


def header_for_complete_api_client() -> list[str]:
    md_lines = []
    md_lines.append('# CompleteAPIClient API Reference\n')
    md_lines.append('This page documents all public methods of the `CompleteAPIClient` class.\n')
    md_lines.append('')
    md_lines.append(
        'For example implemenations please see: '
        '[example_implementation.py]('
        'https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_implementation.py)\n'
    )
    return md_lines


def header_for_xml_decoder() -> list[str]:
    md_lines = []
    md_lines.append('# XML Decoder Reference\n')
    md_lines.append('This page documents the functions of the `xml_decoder` module, which is used to parse XML strings from the API into structured data models.\n')
    md_lines.append('The main function is `parse_xml`, which takes an XML string and returns an instance of the appropriate data model based on the root tag of the XML.\n')
    md_lines.append('The data models are defined in the `plantscreen.xml_models` package and include classes like `Protocol`, `Configuration`, `GroupTiming`, `DataSet`, and `TAnyShapes`.\n')
    md_lines.append('Initial tests showed not all fields of the XML are always pressent, as a result we cannot guaranty the parser will always work.\n')
    md_lines.append('Incase you encouter errors, please check the XML content and make a pull request on the repository so we can improve.\n')
    md_lines.append('In the meantime and as alternative the xml_to_dict function can be used to convert the XML into a dictionary. This works for any XML.\n')
    md_lines.append('')
    md_lines.append('For example implemenations please see: [example_usecase.py](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_usecase.py)\n')
    return md_lines


def main(src_file: Path, doc_path: Path, classname: str):
    """
    Generated a Markdown file documenting all public methods
    of the a class, including their parameters, return types, and descriptions.
    Args:
        src_file (Path): The file containing the class to process
        doc_path (Path): The path to the documentation file
        classname (str): The name of the class to document
            if None, will document all top-level functions in the file instead
    """
    # Build model name to doc link mapping
    docs_dir = Path(__file__).parent.parent / 'docs' / 'docs'
    model_docs = {}
    for fname in docs_dir.iterdir():
        if fname.suffix == '.md':
            model = fname.stem
            model_docs[model] = (
                f'docs/{fname.name}'
            )

    with open(src_file, encoding='utf-8') as f:
        source = f.read()
    # If this is an XML model file, document all classes and their fields
    # ...existing code for API client and xml_decoder...
    if classname == 'CompleteAPIClient':
        md_lines = header_for_complete_api_client()
    elif classname is None and 'xml_decoder' in str(src_file):
        md_lines = header_for_xml_decoder()
    else:
        md_lines = [f'# {classname} Reference\n']
    param_table_header = (
        'Name | Type | Description | Notes\n'
        '------------- | ------------- | ------------- | -------------'
    )
    methods = extract_methods_from_class(source, classname)
    for m in methods:
        ret_link = linkify_return_type(m['returns'], model_docs)
        md_lines.append(f"## {m['name']}\n")
        # ...existing code for method docstring parsing...
        params = []
        desc = ''
        doc = m['docstring']
        if doc:
            lines = doc.strip().splitlines()
            in_args = False
            in_desc = True
            for line in lines:
                stripped_line = line.strip()
                if stripped_line.lower().startswith('args:') or stripped_line.lower().startswith('parameters:'):
                    in_args = True
                    in_desc = False
                    continue
                if stripped_line.lower().startswith('returns:'):
                    in_args = False
                    in_desc = False
                    continue
                if in_args and stripped_line.startswith(('_', '**', '*', 'id', 'device_id', 'round_id', 'tray_id', 'param_id', 'start', 'stop', 'type', 'tag', 'var_date', 'name', 'self', 'response_data', 'default', 'host_index', 'content_type', 'headers', 'request_auth', 'request_timeout')):
                    parts = stripped_line.split(':', 1)
                    if len(parts) == 2:
                        name_type, desc_val = parts
                        name_type = name_type.strip()
                        desc_val = desc_val.strip()
                        if '(' in name_type and ')' in name_type:
                            name, typ = name_type.split('(', 1)
                            name = name.strip()
                            typ = typ.strip(') ')
                        else:
                            name = name_type.strip()
                            typ = ''
                        params.append((name, typ, desc_val))
                elif in_desc and stripped_line:
                    desc += stripped_line + ' '
        if desc:
            md_lines.append(desc.strip() + '\n')
        if params:
            md_lines.append('### Parameters\n')
            md_lines.append(param_table_header)
            for name, typ, desc_val in params:
                md_lines.append(f'**{name}** | **{typ}** | {desc_val} | ')
            md_lines.append('')
        md_lines.append('### Return type\n')
        if ret_link:
            md_lines.append(f'{ret_link}\n')
        elif m['returns']:
            md_lines.append(f'{m["returns"]}\n')
        md_lines.append('---\n')

    # Add navigation links at the bottom
    md_lines.append(
        '[Back to top](#) | [Back to API Endpoints](API_endpoints.md) '
        '| [Back to Models](Models.md) | [Back to README](README.md)\n'
    )

    # Write to file
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f'Generated {doc_path}')


def generate_xml_mdocs():
    """
    Generate documentation for XML models.
    This function processes all XML model files in the plantscreen/xml_models directory,
    extracts the classes and their fields, and generates a Markdown file for each main model.
    The generated Markdown files are saved in the docs directory with links to the models.
    This is separate from the main function because XML models have a different structure
    and we want to document all classes in each file, not just one.
    """
    # XML models: generate docs for all top-level classes in each file
    xml_model_files = {
        'protocol': 'Protocol',
        'configuration': 'Configuration',
        'group_timing': 'GroupTiming',
        'dataset': 'DataSet',
        'tray_type': 'TAnyShapes',
    }
    for filename, main_model in xml_model_files.items():
        file_path = src_path / 'xml_models' / f'{filename}.py'
        print(f"Processing file: {file_path}")
        with open(file_path, encoding='utf-8') as f:
            source = f.read()
        if file_path.parent.name == 'xml_models':
            md_lines = [f'# {file_path.stem.capitalize()} XML Models\n']
            tree = ast.parse(source)
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    md_lines.append(f'\n## {node.name}\n')
                    fields = []
                    for item in node.body:
                        if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                            field_name = item.target.id
                            field_type = ast.unparse(item.annotation) if item.annotation else ''
                            fields.append({'name': field_name, 'type': field_type})
                    if fields:
                        md_lines.append('Name | Type\n------------- | -------------')
                        for field in fields:
                            md_lines.append(f'**{field["name"]}** | **{field["type"]}**')
                        md_lines.append('')
                    else:
                        md_lines.append('_No fields found._\n')
            md_lines.append('\n---')

        md_lines.append(
            '[Back to top](#) | [Back to API Endpoints](../API_endpoints.md) |'
            ' [Back to CompleteAPIClient](../CompleteAPIClient.md) |'
            ' [Back to README](../README.md)\n'
        )

        # Write to file
        model_doc_path = doc_path / 'docs' / f'{main_model}.md'

        with open(model_doc_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md_lines))
        print(f'Generated {model_doc_path}')


if __name__ == '__main__':
    src_path = Path(__file__).parent.parent / 'plantscreen'
    doc_path = Path(__file__).parent.parent / 'docs'

    # Complete API Client
    main(
        src_path / 'complete_api_client.py',
        doc_path / 'CompleteAPIClient.md',
        'CompleteAPIClient'
    )

    # XML decoder
    main(
        src_path / 'xml_decoder.py',
        doc_path / 'XMLDecoder.md',
        None
    )

    generate_xml_mdocs()
