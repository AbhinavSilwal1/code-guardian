import ast
from abc import ABC, abstractmethod


# Base class for all CodeGuardian analyzers
class BaseAnalyzer(ABC):
    # Analyze an AST tree and return findings.
    @abstractmethod
    def analyze(self, tree: ast.AST):
        pass