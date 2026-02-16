# Script to generate docs/CompleteAPIClient.md for mkdocs
import ast
import os
import re

SRC_PATH = os.path.join(os.path.dirname(__file__), '..', 'plantscreen', 'complete_api_client.py')
DOCS_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'CompleteAPIClient.md')

def extract_methods_from_class(source, class_name):
    """Extract all public methods, their signatures, docstrings, and return types from a class in the given source code."""
    tree = ast.parse(source)
    methods = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and not item.name.startswith('_'):
                    # Get signature
                    args = []
                    for arg in item.args.args[1:]:  # skip self
                        arg_str = arg.arg
                        if arg.annotation:
                            arg_str += ': ' + ast.unparse(arg.annotation)
                        args.append(arg_str)
                    # Handle defaults
                    defaults = [None] * (len(item.args.args) - len(item.args.defaults) - 1) + item.args.defaults
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
                    signature = f"{item.name}({', '.join(sig_args)})"
                    # Docstring
                    docstring = ast.get_docstring(item) or ''
                    # Return type
                    returns = ast.unparse(item.returns) if item.returns else ''
                    methods.append({
                        'name': item.name,
                        'signature': signature,
                        'docstring': docstring,
                        'returns': returns,
                    })
    return methods


def linkify_return_type(ret_type, model_docs):
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
            return f'List[[{model}]({link})]'
    m = re.match(r'(?:Optional\[)?(\w+)(?:\])?', base)
    if m:
        model = m.group(1)
        link = model_docs.get(model, None)
        if link:
            return f'[{model}]({link})'
    # Fallback: just return the type
    return ret_type


def main():
    # Build model name to doc link mapping
    docs_dir = os.path.join(os.path.dirname(__file__), '..', 'docs', 'docs')
    model_docs = {}
    for fname in os.listdir(docs_dir):
        if fname.endswith('.md'):
            model = fname.replace('.md', '')
            model_docs[model] = f'docs/{fname}'

    with open(SRC_PATH, encoding='utf-8') as f:
        source = f.read()
    methods = extract_methods_from_class(source, 'CompleteAPIClient')
    # Generate Markdown content
    md_lines = []
    md_lines.append('# CompleteAPIClient API Reference\n')
    md_lines.append('This page documents all public methods of the `CompleteAPIClient` class.\n')
    md_lines.append('')
    md_lines.append('For example implemenations please see: [example_implementation.py](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_implementation.py)\n')


    param_table_header = 'Name | Type | Description | Notes\n------------- | ------------- | ------------- | -------------'
    for m in methods:
        ret_link = linkify_return_type(m['returns'], model_docs)
        md_lines.append(f"## {m['name']}\n")
        # Parse docstring for Args/Parameters
        params = []
        desc = ''
        doc = m['docstring']
        if doc:
            lines = doc.strip().splitlines()
            in_args = False
            in_desc = True
            for line in lines:
                l = line.strip()
                if l.lower().startswith('args:') or l.lower().startswith('parameters:'):
                    in_args = True
                    in_desc = False
                    continue
                if l.lower().startswith('returns:'):
                    in_args = False
                    in_desc = False
                    continue
                if in_args and l.startswith(('_', '**', '*', 'id', 'device_id', 'round_id', 'tray_id', 'param_id', 'start', 'stop', 'type', 'tag', 'var_date', 'name', 'self', 'response_data', 'default', 'host_index', 'content_type', 'headers', 'request_auth', 'request_timeout')):
                    # Try to parse: name (type): description
                    parts = l.split(':', 1)
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
                elif in_desc and l:
                    desc += l + ' '
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
    md_lines.append('[[Back to top]](#) [[Back to API Endpoints](API_endpoints.md)] [[Back to Models](Models.md)] [[Back to README]](README.md)\n')

    # Write to file
    with open(DOCS_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))
    print(f'Generated {DOCS_PATH}')

if __name__ == '__main__':
    main()
