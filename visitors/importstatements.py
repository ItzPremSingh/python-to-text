import ast
from importlib import import_module
from inspect import isclass, isfunction


class ImportStatementsVisitor(ast.NodeVisitor):
    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        module = import_module(node.module) if node.module else None
        for name in node.names:
            entity_type = self._get_entity_type(module, name)
            if name.asname is None:
                print(
                    f"Importing the {name.name} {entity_type} from {node.module} module"
                )
            else:
                print(
                    f"Importing the {name.name} {entity_type} from {node.module} module as {name.asname}"
                )

    def visit_Import(self, node: ast.Import) -> None:
        """
        Visits the ast.Import node.

        This function is called when an ast.Import node is visited.
        It imports the specified module and prints the name of the imported
        entities.
        """
        for name in node.names:
            if name.asname is None:
                print(f"Importing the {name.name} module")
            else:
                print(f"Importing the {name.name} module as {name.asname}")

    def _get_entity_type(self, module, name) -> str:
        """
        Returns the type of the imported entity.

        Args:
            module: The module object.
            name: The name of the imported entity.

        Returns:
            The type of the imported entity.
        """
        imported_entity = getattr(module, name.name)
        if isfunction(imported_entity):
            return "function"
        elif isclass(imported_entity):
            return "class"
        else:
            return "variable"
