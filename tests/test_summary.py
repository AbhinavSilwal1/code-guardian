from pathlib import Path
from codeguardian.models import (
    Issue,
    Severity,
)
from codeguardian.report import SummaryReport


def test_summary_report():
    issues = [
        Issue(
            category="unused_import",
            severity=Severity.LOW,
            message="",
            file=Path("app.py"),
            line=1,
            suggestion="",
        ),
        Issue(
            category="dead_code",
            severity=Severity.HIGH,
            message="",
            file=Path("app.py"),
            line=5,
            suggestion="",
        ),
    ]

    report = SummaryReport(
        3,
        issues,
    )

    text = report.generate()

    assert "Files Scanned: 3" in text
    assert "Total Issues: 2" in text
    assert "LOW: 1" in text
    assert "HIGH: 1" in text
    assert "unused_import: 1" in text