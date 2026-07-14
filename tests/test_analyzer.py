import ast
from codeguardian.analyzers import BaseAnalyzer


class TestAnalyzer(BaseAnalyzer):
    def analyze(self, tree):
        return []


def test_analyzer_contract():
    tree = ast.parse("print('hello')")

    analyzer = TestAnalyzer()

    result = analyzer.analyze(tree)

    assert result == []