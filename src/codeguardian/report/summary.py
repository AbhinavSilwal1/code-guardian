from collections import Counter
from codeguardian.models import Issue


class SummaryReport:
    def __init__(self, files_scanned: int, issues: list[Issue],):
        self.files_scanned = files_scanned
        self.issues = issues

    def severity_counts(self):
        counter = Counter()

        for issue in self.issues:
            counter[issue.severity.value] += 1

        return counter
    
    def category_counts(self):
        counter = Counter()

        for issue in self.issues:
            counter[issue.category] += 1

        return counter
    
    def generate(self):
        severity = self.severity_counts()
        category = self.category_counts()

        lines = []

        lines.append("=" * 50)
        lines.append("CodeGuardian Summary")
        lines.append("=" * 50)
        lines.append("")
        lines.append(f"Files Scanned: {self.files_scanned}")
        lines.append(f"Total Issues: {len(self.issues)}")
        lines.append("")
        lines.append("Issue Breakdown")
        lines.append("----------------")

        for level in ["LOW", "MEDIUM", "HIGH",]:
            lines.append(f"{level}: {severity[level]}")

        lines.append("")
        lines.append("Categories")
        lines.append("----------")

        for name, count in sorted(category.items()):
            lines.append(f"{name}: {count}")

        return "\n".join(lines)