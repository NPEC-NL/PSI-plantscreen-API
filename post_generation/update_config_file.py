import re

# Change the datetime format in API calls from the openAPI default:
# "%Y-%m-%dT%H:%M:%S.%fZ" to PSI's "%Y-%m-%dT%H:%M:%S"


def update_datetime_format(file_path):
    """ Update datetime_format assignment in the given file to the new format.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content, n = re.subn(
        r'self\.datetime_format\s*=\s*"[^"]*"',
        'self.datetime_format = "%Y-%m-%dT%H:%M:%S"',
        content
    )
    if n > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated datetime_format in {file_path}")
    else:
        raise Exception("No datetime_format assignment found to update.")


update_datetime_format('plantscreen/configuration.py')
