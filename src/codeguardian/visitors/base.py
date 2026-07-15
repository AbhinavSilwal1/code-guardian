import ast


# Base AST visitor for CodeGuardian analyzers
class BaseVisitor(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    # Return all collected issues
    def get_issues(self):
        return self.issues