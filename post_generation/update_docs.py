import os
import re


def update_generated_md_files(directory):
    pattern = re.compile(
        r"\[\[Back to Model list\]\]\(\.\./README.md#documentation-for-models\)"
        r" ?"
        r"\[\[Back to API list\]\]\(\.\./README.md#documentation-for-api-endpoints\)"
    )
    parttern2 = re.compile(
        r"\[\[Back to API list\]\]\(\.\./README.md#documentation-for-api-endpoints\)"
        r" ?"
        r"\[\[Back to Model list\]\]\(\.\./README.md#documentation-for-models\)"
    )
    replacement = '[Back to API Endpoints](../API_endpoints.md) [Back to Models](../models.md)'
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_content = pattern.sub(replacement, content)
                new_content = parttern2.sub(replacement, new_content)
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    # print(f"Removed back links from {path}")


# Example usage:
update_generated_md_files('docs')
