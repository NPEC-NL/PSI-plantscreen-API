import os
import re

# Directory to scan for Python files
TARGET_DIR = "plantscreen/models"
IMPORT_LINE = "from pydantic import field_validator\n"


def remove_field_validators():
    """Remove all functions wrapped in @field_validator from Python files in the target directory."""
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                new_lines = []
                skip = False
                skip_lines = 0
                for i, line in enumerate(lines):
                    # Check for field_validator decorator and remove the first function that follows
                    if line.strip().startswith("@field_validator"):
                        # ensure the first function def that follows is removed
                        skip_lines = 1
                        skip = True
                        continue
                    elif skip_lines > 0:
                        skip_lines -= 1
                        continue
                    if skip:
                        # Skip lines until we reach a function end (dedent or end of file)
                        if line.strip().startswith("def "):
                            # This is a new function, stop skipping
                            skip = False
                        elif line.strip() == '' or line.startswith(' '):
                            continue
                        else:
                            skip = False
                    if not skip:
                        new_lines.append(line)
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print(f"Removed field_validator functions from {path}")


def add_pydantic_fieldvalidator_imports():
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                # Check if field_validator is used and not imported
                uses_validator = re.search(r"@field_validator", content)
                has_import = re.search(r"from pydantic import field_validator", content)
                if uses_validator and not has_import:
                    # Insert import after other imports
                    lines = content.splitlines()
                    for i, line in enumerate(lines):
                        if line.strip().startswith("from pydantic") or line.strip().startswith("import pydantic"):
                            insert_at = i + 1
                            break
                    else:
                        # If no pydantic import, insert after docstring or at top
                        insert_at = 0
                    lines.insert(insert_at, IMPORT_LINE)
                    new_content = "\n".join(lines)
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Added field_validator import to {path}")


remove_field_validators()
# add_pydantic_fieldvalidator_imports()
