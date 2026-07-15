import ast
from abc import ABC, abstractmethod


# Base class for all analyzers
class BaseAnalyzer(ABC):
    # Analyze an AST tree
    @abstractmethod
    def analyze(self, tree: ast.AST):
        raise NotImplementedError