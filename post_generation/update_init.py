"""
Script to auto-import all models from plantscreen/xml_models and
functions from plantscreen/xml_decoder
into plantscreen/__init__.py for easier top-level access.
"""
import os


def add_to_init(import_line: str, symbol: str):
    """
    Add an import line and symbol to __all__ in plantscreen/__init__.py if not already present.
    Args:
        import_line (str): The import statement to add (with newline).
        symbol (str): The symbol (class/function) to add to __all__ (string, no quotes).
    """
    # Add import if not present
    if not any(symbol in line and "import" in line for line in init_lines):
        # Find first non-comment, non-docstring line after imports
        insert_at = 0
        for i, line in enumerate(init_lines):
            if line.strip().startswith("from") or line.strip().startswith("import"):
                insert_at = i + 1
        init_lines.insert(insert_at, import_line)
    # Add to __all__ if not present
    for i, line in enumerate(init_lines):
        if line.strip().startswith("__all__"):
            # Find the closing bracket
            for j in range(i, len(init_lines)):
                if "]" in init_lines[j]:
                    if f'"{symbol}"' not in ''.join(init_lines[i:j+1]):
                        # Insert before closing bracket
                        init_lines.insert(j, f'    "{symbol}",\n')
                    break
            break
    print(f"Added {symbol} to __init__.py")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    init_path = os.path.join(os.path.dirname(script_dir), "plantscreen", "__init__.py")
    with open(init_path, "r", encoding="utf-8") as f:
        init_lines = f.readlines()

    to_import = [
        {"CompleteAPIClient": "from plantscreen.complete_api_client import CompleteAPIClient\n"},
        {"parse_xml": "from plantscreen.xml_decoder import parse_xml\n"},
        {"Configuration": "from plantscreen.xml_models.configuration import Configuration\n"},
        {"GroupTiming": "from plantscreen.xml_models.group_timing import GroupTiming\n"},
        {"Protocol": "from plantscreen.xml_models.protocol import Protocol\n"},
        {"SystemConfig": "from plantscreen.xml_models.system_config import Configuration as SystemConfig\n"},
        {"TAnyShapes": "from plantscreen.xml_models.tray_type import TAnyShapes\n"},
        {"DataSet": "from plantscreen.xml_models.dataset import DataSet\n"},
    ]
    for entry in to_import:
        for symbol, import_line in entry.items():
            add_to_init(import_line, symbol)

    with open(init_path, "w", encoding="utf-8") as f:
        f.writelines(init_lines)
