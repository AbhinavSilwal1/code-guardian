from pathlib import Path
from codeguardian.engine import AnalysisEngine
from codeguardian.report import SummaryReport
from codeguardian.scanner import find_python_files
from codeguardian.formatters import issue_to_dict


def analyze_project(path: str):
    project_path = Path(path)

    engine = AnalysisEngine()

    issues = engine.analyze_repository(project_path)

    python_files = find_python_files(project_path)

    report = SummaryReport(
        len(python_files),
        issues,
    )

    return {
        "summary": {
            "files_scanned": len(python_files),
            "total_issues": len(issues),
            "severity_counts": dict(
                report.severity_counts()
            ),
            "category_counts": dict(
                report.category_counts()
            ),
        },
        "issues": [
            issue_to_dict(issue)
            for issue in issues
        ],
    }