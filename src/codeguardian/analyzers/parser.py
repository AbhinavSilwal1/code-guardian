import ast
from pathlib import Path

# Parses Python files into AST trees
class PythonParser:
    # Parse a Python file and return its AST tree
    def parse_file(self, file_path: Path):
        try:
            source = file_path.read_text(encoding="utf-8")
            tree = ast.parse(source)
            return tree

        except SyntaxError as error:
            return None