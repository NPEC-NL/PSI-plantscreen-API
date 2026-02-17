import re


NEW_METHOD = """    def file(
        self,
        path: str,
        _request_timeout: float = 300,
        _headers: Optional[Dict[StrictStr, Any]] = None
    ) -> BytesIO:
        \"\"\" Returns the content of a file as bytesio object

        Args:
            path (str): Path of the file to download

        Return:
            io.BytesIO

        \"\"\"
        s = Session()
        data = BytesIO()
        with s.get(f"{self.api_client.configuration.host}/file", params={"path": path}, headers=_headers, stream=True, timeout=_request_timeout) as resp:
            if resp.status_code != 200:
                raise Exception(f"Failed to download file: {resp.status_code} {resp.reason}")
            else:
                data.write(resp.content)
                data.seek(0)
        return data
"""


def replace_file_method(target_file: str):
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Add imports if not present
    import_lines = 'from requests import Session\nfrom io import BytesIO\n'
    if 'from requests import Session' not in content:
        content = import_lines + content
    # Regex to match the file method definition and its body
    pattern = re.compile(r'@validate_call\s+def file\([^\)]*\)[\s\S]+?return self.api_client.response_deserialize\([^\)]*\)\.[^\n]+', re.MULTILINE)
    new_content, count = pattern.subn(NEW_METHOD, content)
    if count == 0:
        raise Exception('No file method found to replace.')
    else:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('Replaced file method and added imports in file_api.py')


if __name__ == '__main__':
    replace_file_method('plantscreen/api/file_api.py')
