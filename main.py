from rc import rc
import matplotlib as mpl
import numpy as py
import ast
import astor
import os

filename = 'example.py'
with open(filename) as f:
    content = f.read()
parsed = ast.parse(content)

function_defs = [node for node in parsed.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]

import_lines = []
imports = {}
for node in parsed.body:
    if isinstance(node, ast.ImportFrom):
        for alias in node.names:
            name = alias.name
            import_lines.append(astor.to_source(node).replace(node.module, name).strip())
            imports[name] = node.module
    elif isinstance(node, ast.Import):
        for alias in node.names:
            name = alias.name
            import_lines.append(astor.to_source(node).strip())
            imports[name] = name

for function_def in function_defs:
    function_name = function_def.name
    api_filename = f"{function_name}.py"

    required_imports = set()
    for node in ast.walk(function_def):
        if isinstance(node, ast.Name) and node.id in imports:
            required_imports.add(imports[node.id])

    with open(api_filename, "w") as api_file:
        for i, line in enumerate(import_lines):
            for imp in required_imports:
                if imp in line:
                    api_file.write(line + "\n")
                    import_lines[i] = ""

        api_file.write(astor.to_source(function_def))

        with open(api_filename) as f:
            print(f"\n{api_filename}:")
            print(f.read())

# Update API files with elements from list1
for line in import_lines:
    last_word = line.split()[-1]
    for api_file in os.listdir('.'):
        if api_file.endswith('.py'):
            with open(api_file) as f:
                api_contents = f.read()

                if last_word in api_contents:
                    with open(api_file, "r+") as f:
                        contents = f.read()
                        f.seek(0, 0)
                        f.write(line.rstrip('\r\n') + '\n' + contents)

# Print updated API files
for api_file in os.listdir('.'):
    if api_file.endswith('.py'):
        with open(api_file) as f:
            print(f"\n{api_file}:")
            print(f.read())