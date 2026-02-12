import re


"""
experiment_id, owner_id and profile_id methods in CompleteAPIClient return a list of
objects with the id as a field. This helper functions update the return type of
these methods to return a list of ints instead, by changing the method to extract
the id field from each object in the list and return that instead.
"""


def update_experiment_id_return(content: str) -> str:
    pattern = re.compile(
        r"def experiment_id\(self, _request_timeout=None, _request_auth=None, "
        r"_content_type=None, _headers=None, _host_index=0\):\n\s+"
        r"result = self._ExperimentApi.experiment_id\(_request_timeout, "
        r"_request_auth, _content_type, _headers, _host_index\)\n\s+"
        r"return getattr\(result, \"json_experiment_id_result\", None\)"
    )
    replacement = (
        "def experiment_id(self, _request_timeout=None, _request_auth=None, "
        "_content_type=None, _headers=None, _host_index=0) -> list[int]:\n"
        "        result = self._ExperimentApi.experiment_id("
        "_request_timeout, _request_auth, _content_type, _headers, _host_index)\n"
        "        temp = getattr(result, \"json_experiment_id_result\", None)\n"
        "        if temp is not None:\n"
        "            return [x.experiment_id for x in temp]\n"
        "        else:\n"
        "            return []"
    )
    new_content, n = pattern.subn(replacement, content)
    if n > 0:
        print("Updated experiment_id method")
    else:
        raise Exception("No matching experiment_id method found to update.")
    return new_content


def update_owner_id_return(content: str) -> str:
    pattern = re.compile(
        r'def owner_id\(self, _request_timeout=None, _request_auth=None, '
        r'_content_type=None, _headers=None, _host_index=0\):\n\s+'
        r'result = self._ExperimentApi.owner_id\(_request_timeout, '
        r'_request_auth, _content_type, _headers, _host_index\)\n\s+'
        r'return getattr\(result, "json_owner_id_result", None\)'
    )
    replacement = (
        'def owner_id(self, _request_timeout=None, _request_auth=None, '
        '_content_type=None, _headers=None, _host_index=0) -> list[int]:\n'
        '        result = self._ExperimentApi.owner_id('
        '_request_timeout, _request_auth, _content_type, _headers, _host_index)\n'
        '        temp = getattr(result, "json_owner_id_result", None)\n'
        '        if temp is not None:\n'
        '            return [x.owner_id for x in temp]\n'
        '        else:\n'
        '            return []'
    )
    new_content, n = pattern.subn(replacement, content)
    if n > 0:
        print("Updated owner_id method")
    else:
        raise Exception("No matching owner_id method found to update.")
    return new_content


def update_profile_id_return(content: str) -> str:
    import re
    pattern = re.compile(
        (
            r'def profile_id\(self, _request_timeout=None, _request_auth=None, '
            r'_content_type=None, _headers=None, _host_index=0\):\n\s+'
            r'result = self._ProfileApi.profile_id\(_request_timeout, _request_auth, '
            r'_content_type, _headers, _host_index\)\n\s+'
            r'return getattr\(result, "json_system_profile_id_result", None\)'
        )
    )
    replacement = (
        'def profile_id(self, _request_timeout=None, _request_auth=None, '
        '_content_type=None, _headers=None, _host_index=0) -> list[int]:\n'
        '        result = self._ProfileApi.profile_id('
        '_request_timeout, _request_auth, _content_type, _headers, _host_index)\n'
        '        temp = getattr(result, "json_system_profile_id_result", None)\n'
        '        if temp is not None:\n'
        '            return [x.profile_id for x in temp]\n'
        '        else:\n'
        '            return []'
    )
    new_content, n = pattern.subn(replacement, content)
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
