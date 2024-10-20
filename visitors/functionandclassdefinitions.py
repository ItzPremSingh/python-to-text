import ast


class FunctionAndClassDefinitionsVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """
        Visits the ast.FunctionDef node and prints the function details in a way
        that is easy for non-programmers to understand.
        """
        name = node.name
        args = [arg.arg for arg in node.args.args]
        varargs = node.args.vararg.arg if node.args.vararg else None
        kwargs = node.args.kwarg.arg if node.args.kwarg else None
        defaults = (
            [ast.unparse(d) for d in node.args.defaults] if node.args.defaults else None
        )
        returns = ast.unparse(node.returns) if node.returns else None
        decorators = (
            [ast.unparse(decorator) for decorator in node.decorator_list]
            if node.decorator_list
            else []
        )

        print(
            f"Function {name} takes arguments {', '.join(args)} "
            f"with default values {', '.join(defaults) if defaults else 'None'} "
            f"and is decorated with {', '.join(decorators)}; "
            f"it returns {returns}."
        )

        for body in node.body:
            self.visit(body)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        # TODO: Implement visit logic for AsyncFunctionDef
        pass

    def visit_ClassDef(self, node: ast.ClassDef):
        # TODO: Implement visit logic for ClassDef
        pass
