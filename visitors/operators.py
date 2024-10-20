import ast


class OperatorsVisitor(ast.NodeVisitor):
    def visit_Add(self, node: ast.Add) -> str:
        """Visits the ast.Add node.

        This function is called when an ast.Add node is visited.
        It returns the string representation of the addition operator.
        """
        return "+"

    def visit_Sub(self, node: ast.Sub) -> str:
        """Visits the ast.Sub node.

        This function is called when an ast.Sub node is visited.
        It returns the string representation of the subtraction operator.
        """
        return "-"

    def visit_Mult(self, node: ast.Mult) -> str:
        """Visits the ast.Mult node.

        This function is called when an ast.Mult node is visited.
        It returns the string representation of the multiplication operator.
        """
        return "*"

    def visit_Div(self, node: ast.Div) -> str:
        """Visits the ast.Div node.

        This function is called when an ast.Div node is visited.
        It returns the string representation of the division operator.
        """
        return "/"

    def visit_FloorDiv(self, node: ast.FloorDiv) -> str:
        """Visits the ast.FloorDiv node.

        This function is called when an ast.FloorDiv node is visited.
        It returns the string representation of the floor division operator.
        """
        return "//"

    def visit_Mod(self, node: ast.Mod) -> str:
        """Visits the ast.Mod node.

        This function is called when an ast.Mod node is visited.
        It returns the string representation of the modulo operator.
        """
        return "%"

    def visit_Pow(self, node: ast.Pow) -> str:
        """Visits the ast.Pow node.

        This function is called when an ast.Pow node is visited.
        It returns the string representation of the exponentiation operator.
        """
        return "**"

    def visit_LShift(self, node: ast.LShift) -> str:
        """Visits the ast.LShift node.

        This function is called when an ast.LShift node is visited.
        It returns the string representation of the left shift operator.
        """
        return "<<"

    def visit_RShift(self, node: ast.RShift) -> str:
        """Visits the ast.RShift node.

        This function is called when an ast.RShift node is visited.
        It returns the string representation of the right shift operator.
        """
        return ">>"

    def visit_BitAnd(self, node: ast.BitAnd) -> str:
        """Visits the ast.BitAnd node.

        This function is called when an ast.BitAnd node is visited.
        It returns the string representation of the bitwise and operator.
        """
        return "&"

    def visit_BitOr(self, node: ast.BitOr) -> str:
        """Visits the ast.BitOr node.

        This function is called when an ast.BitOr node is visited.
        It returns the string representation of the bitwise or operator.
        """
        return "|"

    def visit_BitXor(self, node: ast.BitXor) -> str:
        """Visits the ast.BitXor node.

        This function is called when an ast.BitXor node is visited.
        It returns the string representation of the bitwise xor operator.
        """
        return "^"

    def visit_UAdd(self, node: ast.UAdd) -> str:
        """Visits the ast.UAdd node.

        This function is called when an ast.UAdd node is visited.
        It returns the string representation of the unary plus operator.
        """
        return "+"

    def visit_USub(self, node: ast.USub) -> str:
        """Visits the ast.USub node.

        This function is called when an ast.USub node is visited.
        It returns the string representation of the unary minus operator.
        """
        return "-"

    def visit_Not(self, node: ast.Not) -> str:
        """Visits the ast.Not node.

        This function is called when an ast.Not node is visited.
        It returns the string representation of the logical not operator.
        """
        return "not"

    def visit_And(self, node: ast.And) -> str:
        """Visits the ast.And node.

        This function is called when an ast.And node is visited.
        It returns the string representation of the logical and operator.
        """
        return "and"

    def visit_Or(self, node: ast.Or) -> str:
        """Visits the ast.Or node.

        This function is called when an ast.Or node is visited.
        It returns the string representation of the logical or operator.
        """
        return "or"

    def visit_In(self, node: ast.In) -> str:
        """Visits the ast.In node.

        This function is called when an ast.In node is visited.
        It returns the string representation of the membership test operator.
        """
        return "in"

    def visit_NotIn(self, node: ast.NotIn) -> str:
        """Visits the ast.NotIn node.

        This function is called when an ast.NotIn node is visited.
        It returns the string representation of the not in operator.
        """
        return "not in"

    def visit_Is(self, node: ast.Is) -> str:
        """Visits the ast.Is node.

        This function is called when an ast.Is node is visited.
        It returns the string representation of the is operator.
        """
        return "is"

    def visit_IsNot(self, node: ast.IsNot) -> str:
        """Visits the ast.IsNot node.

        This function is called when an ast.IsNot node is visited.
        It returns the string representation of the is not operator.
        """
        return "is not"

    def visit_Eq(self, node: ast.Eq) -> str:
        """Visits the ast.Eq node.

        This function is called when an ast.Eq node is visited.
        It returns the string representation of the equality comparison operator.
        """
        return "=="

    def visit_NotEq(self, node: ast.NotEq) -> str:
        """Visits the ast.NotEq node.

        This function is called when an ast.NotEq node is visited.
        It returns the string representation of the inequality comparison operator.
        """
        return "!="

    def visit_Gt(self, node: ast.Gt) -> str:
        """Visits the ast.Gt node.

        This function is called when an ast.Gt node is visited.
        It returns the string representation of the greater than comparison operator.
        """
        return ">"

    def visit_Lt(self, node: ast.Lt) -> str:
        """Visits the ast.Lt node.

        This function is called when an ast.Lt node is visited.
        It returns the string representation of the less than comparison operator.
        """
        return "<"

    def visit_GtE(self, node: ast.GtE) -> str:
        """Visits the ast.GtE node.

        This function is called when an ast.GtE node is visited.
        It returns the string representation of the greater than or equal comparison operator.
        """
        return ">="

    def visit_LtE(self, node: ast.LtE) -> str:
        """Visits the ast.LtE node.

        This function is called when an ast.LtE node is visited.
        It returns the string representation of the less than or equal comparison operator.
        """
        return "<="
