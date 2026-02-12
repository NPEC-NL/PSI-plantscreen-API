# Function to add docstrings to each function in plantscreen/complete_api_client.py
import ast


def add_docstrings_to_complete_api_client():
    filename = "plantscreen/complete_api_client.py"
    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source)

    class CompleteAPIClientVisitor(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            # Skip if already has a docstring
            if ast.get_docstring(node):
                return node
            # Build docstring
            params = []
            for arg in node.args.args[1:]:  # skip 'self'
                param_name = arg.arg
                param_type = 'Any'
                if arg.annotation:
                    param_type = ast.unparse(arg.annotation)
                params.append(f"{param_name} ({param_type})")
            returns = 'Any'
            if node.returns:
                returns = ast.unparse(node.returns)
            docstring = ["        Parameters:"]
            docstring += [f"            {p}" for p in params]
            docstring += ["        Returns:"]
            docstring += [f"            {returns}", "        \"\"\""]
            node.body.insert(0, ast.Expr(value=ast.Constant(value="\n" + "\n".join(docstring))))
            return node
    for n in tree.body:
        if isinstance(n, ast.ClassDef) and n.name == "CompleteAPIClient":
            CompleteAPIClientVisitor().visit(n)
    new_source = ast.unparse(tree)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_source)


add_docstrings_to_complete_api_client()
