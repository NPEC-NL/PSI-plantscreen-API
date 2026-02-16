import re


"""
experiment_id, owner_id and profile_id methods in CompleteAPIClient return a list of
objects with the id as a field. This helper functions update the return type of
these methods to return a list of ints instead, by changing the method to extract
the id field from each object in the list and return that instead.
"""


def update_experiment_id_return(content: str) -> str:
    pattern = re.compile(
        (
            r"def experiment_id\(self, _request_timeout: Optional\[Union\[float, "
            r"Tuple\[float, float\]\]\] = None, "
            r"_request_auth: Optional\[Dict\[str, Any\]] = None, "
            r"_content_type: Optional\[str\] = None, "
            r"_headers: Optional\[Dict\[str, Any\]] = None, "
            r"_host_index: int = 0\) -> List\[ExperimentIDWrapper\]:\n"
            r'(\s+"""[\s\S]*?"""\n)?'
            r'(\s+)'
            r'result = self\._ExperimentApi\.experiment_id\('
            r'_request_timeout, _request_auth, _content_type, _headers, _host_index\)\n'
            r'\s+return getattr\(result, "json_experiment_id_result", None\)'
        )
    )

    def repl(match):
        funcdef = (
            'def experiment_id('
            'self,'
            ' _request_timeout: Optional[Union[float, Tuple[float, float]]] = None,'
            ' _request_auth: Optional[Dict[str, Any]] = None,'
            ' _content_type: Optional[str] = None,'
            ' _headers: Optional[Dict[str, Any]] = None,'
            ' _host_index: int = 0'
            ') -> list[int]:\n'
        )
        docstring = match.group(1) or ''
        indent = match.group(2)
        if docstring:
            docstring = re.sub(r'Returns:\n\s*List\[.*?\]: Model class instance\.',
                               f'Returns:\n{indent}    List[int]: list of ids.',
                               docstring
            )
        body = (
            f'{indent}result = self._ExperimentApi.experiment_id(_request_timeout, _request_auth, _content_type, _headers, _host_index)\n'
            f'{indent}temp = getattr(result, "json_experiment_id_result", None)\n'
            f'{indent}if temp is not None:\n'
            f'{indent}    return [x.experiment_id for x in temp]\n'
            f'{indent}else:\n'
            f'{indent}    return []'
        )
        return funcdef + (docstring if docstring else '') + body
    new_content, n = pattern.subn(repl, content)
    if n > 0:
        print("Updated experiment_id method")
    else:
        raise Exception("No matching experiment_id method found to update.")
    return new_content


def update_owner_id_return(content: str) -> str:
    pattern = re.compile(
        (
            r'def owner_id\(self, _request_timeout: Optional\[Union\[float, '
            r'Tuple\[float, float\]\]\] = None, '
            r'_request_auth: Optional\[Dict\[str, Any\]] = None, '
            r'_content_type: Optional\[str\] = None, '
            r'_headers: Optional\[Dict\[str, Any\]] = None, '
            r'_host_index: int = 0\) -> List\[OwnerIDWrapper\]:\n'
            r'(\s+"""[\s\S]*?"""\n)?'
            r'(\s+)'
            r'result = self\._ExperimentApi\.owner_id\('
            r'_request_timeout, _request_auth, _content_type, _headers, _host_index\)\n'
            r'\s+return getattr\(result, "json_owner_id_result", None\)'
        )
    )

    def repl(match):
        funcdef = (
            'def owner_id('
            'self,'
            ' _request_timeout: Optional[Union[float, Tuple[float, float]]] = None,'
            ' _request_auth: Optional[Dict[str, Any]] = None,'
            ' _content_type: Optional[str] = None,'
            ' _headers: Optional[Dict[str, Any]] = None,'
            ' _host_index: int = 0'
            ') -> list[int]:\n'
        )
        docstring = match.group(1) or ''
        indent = match.group(2)
        if docstring:
            docstring = re.sub(r'Returns:\n\s*List\[.*?\]: Model class instance\.',
                               f'Returns:\n{indent}    List[int]: list of ids.',
                               docstring
            )
        body = (
            f'{indent}result = self._ExperimentApi.owner_id(_request_timeout, _request_auth, _content_type, _headers, _host_index)\n'
            f'{indent}temp = getattr(result, "json_owner_id_result", None)\n'
            f'{indent}if temp is not None:\n'
            f'{indent}    return [x.owner_id for x in temp]\n'
            f'{indent}else:\n'
            f'{indent}    return []'
        )
        return funcdef + (docstring if docstring else '') + body
    new_content, n = pattern.subn(repl, content)
    if n > 0:
        print("Updated owner_id method")
    else:
        raise Exception("No matching owner_id method found to update.")
    return new_content


def update_profile_id_return(content: str) -> str:
    pattern = re.compile(
        (
            r'def profile_id\(self, _request_timeout: Optional\[Union\[float, '
            r'Tuple\[float, float\]\]\] = None, '
            r'_request_auth: Optional\[Dict\[str, Any\]] = None, '
            r'_content_type: Optional\[str\] = None, '
            r'_headers: Optional\[Dict\[str, Any\]] = None, '
            r'_host_index: int = 0\) -> List\[ProfileIDWrapper\]:\n'
            r'(\s+"""[\s\S]*?"""\n)?'
            r'(\s+)'
            r'result = self\._ProfileApi\.profile_id\(_request_timeout, '
            r'_request_auth, _content_type, _headers, _host_index\)\n'
            r'\s+return getattr\(result, "json_system_profile_id_result", None\)'
        )
    )

    def repl(match):
        funcdef = (
            'def profile_id('
            'self,'
            ' _request_timeout: Optional[Union[float, Tuple[float, float]]] = None,'
            ' _request_auth: Optional[Dict[str, Any]] = None,'
            ' _content_type: Optional[str] = None,'
            ' _headers: Optional[Dict[str, Any]] = None,'
            ' _host_index: int = 0'
            ') -> list[int]:\n'
        )
        docstring = match.group(1) or ''
        indent = match.group(2)
        if docstring:
            docstring = re.sub(r'Returns:\n\s*List\[.*?\]: Model class instance\.',
                               f'Returns:\n{indent}    List[int]: list of ids.',
                               docstring
            )
        body = (
            f'{indent}result = self._ProfileApi.profile_id(_request_timeout, _request_auth, _content_type, _headers, _host_index)\n'
            f'{indent}temp = getattr(result, "json_system_profile_id_result", None)\n'
            f'{indent}if temp is not None:\n'
            f'{indent}    return [x.profile_id for x in temp]\n'
            f'{indent}else:\n'
            f'{indent}    return []'
        )
        return funcdef + (docstring if docstring else '') + body
    new_content, n = pattern.subn(repl, content)
    if n > 0:
        print("Updated profile_id method")
    else:
        raise Exception("No matching profile_id method found to update.")
    return new_content


# Update CompleteAPIClient
source_file = 'plantscreen/complete_api_client.py'
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = update_experiment_id_return(content)
new_content = update_owner_id_return(new_content)
new_content = update_profile_id_return(new_content)

with open(source_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
