from pathlib import Path
from codeguardian.analyzers.parser import PythonParser


def test_parser_reads_python_file(tmp_path):
    python_file = tmp_path / "example.py"
    python_file.write_text("def hello():\n    pass")

    parser = PythonParser()

    tree = parser.parse_file(python_file)

    assert tree is not None


def test_parser_handles_invalid_python(tmp_path):
    python_file = tmp_path / "bad.py"
    python_file.write_text("def broken(:")

    parser = PythonParser()

    tree = parser.parse_file(python_file)

    assert tree is None