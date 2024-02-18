from os import walk, path

""" Converts the content of the docs folder to the mkdocs format 
"""
for root, dirs, files in walk("docs"):
    prepend_spaces = ""
    for i in range(0, len(root.split('\\'))):
        prepend_spaces += '  '
    file_path = root.split('\\')[1:]
    file_path = '/'.join(file_path)
    if len(file_path) > 0:
        file_path += '/'
    folder = root.split('\\')[-1]
    print(f"{prepend_spaces}- {folder}:")
    prepend_spaces += '  '
    for file in files:
        if file == 'style.css':
            continue
        print(f"{prepend_spaces}- {path.splitext(file)[0]}: {file_path}{file}")
