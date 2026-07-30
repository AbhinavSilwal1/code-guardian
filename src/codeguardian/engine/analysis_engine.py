from pathlib import Path
from codeguardian.analyzers.unused_import import UnusedImportAnalyzer
from codeguardian.analyzers.long_function import LongFunctionAnalyzer
from codeguardian.analyzers.too_many_arguments import TooManyArgumentsAnalyzer
from codeguardian.analyzers.dead_code import DeadCodeAnalyzer
from codeguardian.analyzers.circular_dependency import CircularDependencyAnalyzer
from codeguardian.analyzers.parser import PythonParser
from codeguardian.graph import DependencyGraphBuilder
from codeguardian.scanner import find_python_files
from codeguardian.config import load_config


class AnalysisEngine:
    def __init__(self, config=None):
        self.parser = PythonParser()

        self.config = config if config is not None else load_config()

        self.analyzers = []

        rules = self.config["rules"]

        if rules["unused_import"]["enabled"]:
            self.analyzers.append(UnusedImportAnalyzer())

        if rules["long_function"]["enabled"]:
            self.analyzers.append(
                LongFunctionAnalyzer(
                    max_lines=
                    rules["long_function"]["max_lines"]
                )
            )

        if rules["too_many_arguments"]["enabled"]:
            self.analyzers.append(
                TooManyArgumentsAnalyzer(
                    max_arguments=
                    rules["too_many_arguments"]["max_arguments"]
                )
            )

        if rules["dead_code"]["enabled"]:
            self.analyzers.append(
                DeadCodeAnalyzer()
            )

    def analyze_repository(self, directory: Path):
        issues = []

        files = find_python_files(directory)

        for file in files:
            tree = self.parser.parse_file(file)

            if tree is None:
                continue

            for analyzer in self.analyzers:

                issues.extend(
                    analyzer.analyze(
                        tree,
                        file
                    )
                )

        rules = self.config["rules"]

        if rules["circular_dependency"]["enabled"]:
            graph = DependencyGraphBuilder().build(files)

            circular_analyzer = (CircularDependencyAnalyzer(graph))

            issues.extend(circular_analyzer.analyze())

        return issues