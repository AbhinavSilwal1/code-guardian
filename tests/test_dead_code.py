import ast
from pathlib import Path
from codeguardian.analyzers.dead_code import DeadCodeAnalyzer


def test_dead_function():
    tree = ast.parse(
        """
def helper():
    pass


def greet():
    print("Hello")


greet()
"""
    )

    analyzer = DeadCodeAnalyzer()

    issues = analyzer.analyze(
        tree,
        Path("test.py"),
    )

    assert len(issues) == 1
    assert issues[0].category == "dead_code"


def test_used_function():
    tree = ast.parse(
        """
def helper():
    print("Hello")


helper()
"""
    )

    analyzer = DeadCodeAnalyzer()

    issues = analyzer.analyze(
        tree,
        Path("test.py"),
    )

    assert len(issues) == 0


def test_main_function_is_ignored():
    tree = ast.parse(
        """
def main():
    print("Hello")
"""
    )

    analyzer = DeadCodeAnalyzer()

    issues = analyzer.analyze(
        tree,
        Path("test.py"),
    )

    assert len(issues) == 0