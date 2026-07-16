import ast
from pathlib import Path
from codeguardian.analyzers import BaseAnalyzer
from codeguardian.models import Issue, Severity
from codeguardian.visitors import BaseVisitor


class DeadCodeVisitor(BaseVisitor):
    def __init__(self):
        super().__init__()

        self.defined_functions = {}
        self.called_functions = set()

    def visit_FunctionDef(self, node):
        self.defined_functions[node.name] = node
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.called_functions.add(node.func.id)

        self.generic_visit(node)


class DeadCodeAnalyzer(BaseAnalyzer):
    def analyze(self, tree: ast.AST, file_path: Path):
        visitor = DeadCodeVisitor()
        visitor.visit(tree)

        issues = []

        ignored_functions = {
            "main",
        }

        for name, node in visitor.defined_functions.items():
            if name in ignored_functions:
                continue

            if name not in visitor.called_functions:
                issues.append(
                    Issue(
                        category="dead_code",
                        severity=Severity.LOW,
                        message=f"Function '{name}' is never called.",
                        file=file_path,
                        line=node.lineno,
                        suggestion=(
                            "Remove the function or "
                            "integrate it into the codebase."
                        ),
                    )
                )

        return issues