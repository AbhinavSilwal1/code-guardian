from pathlib import Path
from codeguardian.models import Issue, Severity


def test_issue_creation():
    issue = Issue(
        category="security",
        severity=Severity.HIGH,
        message="Test issue",
        file=Path("test.py"),
        line=5
    )

    assert issue.category == "security"
    assert issue.severity == Severity.HIGH
    assert issue.line == 5


def test_issue_string():
    issue = Issue(
        category="security",
        severity=Severity.HIGH,
        message="Dangerous code detected.",
        file=Path("main.py"),
        line=10,
        suggestion="Review this code."
    )

    output = str(issue)

    assert "security" in output
    assert "HIGH" in output
    assert "main.py" in output