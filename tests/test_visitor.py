import ast
from codeguardian.visitors import BaseVisitor


def test_base_visitor():
    visitor = BaseVisitor()

    tree = ast.parse("print('hello')")

    visitor.visit(tree)

    assert visitor.get_issues() == []