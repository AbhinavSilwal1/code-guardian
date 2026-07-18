import typer
from rich.console import Console
from codeguardian.scanner import find_python_files
from pathlib import Path
from codeguardian.engine import AnalysisEngine
from rich.panel import Panel
from codeguardian.config import load_config
from codeguardian.formatters import issues_to_json
from codeguardian.report import SummaryReport


app = typer.Typer()
console = Console()


def severity_color(severity):
    colors = {
        "HIGH": "red",
        "MEDIUM": "yellow",
        "LOW": "green",
    }

    return colors.get(
        severity.value,
        "white"
    )


# Callback function
@app.callback()
def callback():
    pass


# Scan a project directory
@app.command()
def scan(
    path: str,
    json_output: bool = typer.Option(
        False,
        "--json",
        help="Output issues as JSON.",
    ),
    config: Path = typer.Option(
        Path("codeguardian.yml"),
        "--config",
        help="Configuration file.",
    ),
):
    config_data = load_config(config)
    engine = AnalysisEngine()
    issues = engine.analyze_repository(Path(path))
    python_files = find_python_files(path)

    if json_output:
        print(issues_to_json(issues))
        return

    console.print("\n[bold blue]Scanning project...[/bold blue]\n")
    if not issues:
        console.print("[green]✓ No issues found.[/green]")
    else:
        console.print(f"[yellow]Found {len(issues)} issue(s):[/yellow]\n")
    
    for issue in issues:
        color = severity_color(issue.severity)

        console.print(
            Panel(
                str(issue),
                title=f"[{color}]{issue.category}[/{color}]",
                expand=False
            )
        )
    
    report = SummaryReport(
        len(python_files),
        issues,
    )

    console.print()
    console.print(report.generate())


if __name__ == "__main__":
    app()