# 🛡️ CodeGuardian

AST-powered static analysis platform for Python projects featuring configurable analysis rules, dependency analysis, circular dependency detection, an interactive React + TypeScript dashboard, and JSON reporting.


## 🧠 Overview

CodeGuardian is a static analysis platform that helps developers identify common code quality issues before they become technical debt.

The core analysis engine uses Python's Abstract Syntax Tree (AST) to detect structural issues such as unused imports, dead code, long functions, excessive function arguments, and circular dependencies.

Starting with version 1.1.0, CodeGuardian combines its static analysis engine with an interactive React + TypeScript dashboard powered by a FastAPI backend. Developers can analyze Python projects, review summary statistics, explore issues in detail, filter and sort results, and export complete analysis reports as JSON.

CodeGuardian can analyze any accessible Python project directory, including projects located outside the CodeGuardian repository itself.

The project is designed with a modular architecture that allows additional analyzers, reporting formats, and integrations to be added in future releases.


## 🚀 Features

### Static Analysis

- Detect unused imports
- Detect dead code
- Detect long functions
- Detect functions with too many parameters
- Build module dependency graphs
- Detect circular dependencies

### Interactive Dashboard

- Analyze Python projects through a React + TypeScript web interface
- Analyze projects located outside the CodeGuardian repository
- View project summary statistics
- View total files scanned and total issues detected
- View issue counts by severity
- Explore severity distribution through visual breakdowns
- Expand individual issues to view detailed messages and suggestions

### Analysis & Issue Management

- Search issues by relevant information
- Filter issues by severity
- Filter issues by category
- Sort issues by severity
- Expand and collapse individual issue details
- Copy file paths directly from issue results
- Copy file locations including line numbers
- Copy complete issue details for easier debugging and sharing
- Clear error messages for invalid or missing project paths
- Dedicated empty states for projects with no detected issues

### Reporting

- Rich terminal output
- JSON output for automation and CI pipelines
- Project summary reports
- Export complete dashboard analysis results as JSON

### Configuration

- YAML configuration support
- Enable or disable individual rules
- Customize rule thresholds

### Developer Experience

- Modular architecture
- FastAPI backend
- React + TypeScript frontend
- Comprehensive pytest test suite
- Command-line interface powered by Typer
- Interactive dashboard powered by Tailwind CSS


## 🛠 Technologies Used

### Backend

- Python
- FastAPI
- AST (Abstract Syntax Tree)
- Typer
- Rich
- PyYAML

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS

### Testing

- pytest


## 📦 How To Run

### Clone the Repository

```bash
git clone https://github.com/AbhinavSilwal1/code-guardian.git
cd code-guardian
```

### Set up the Backend

Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:
```bash
pip install -r requirements.txt
```

### Start the Backend

From the CodeGuardian project root directory, start the FastAPI server:
```bash
uvicorn backend.app.main:app --reload
```

The backend API will be available at:
```text
http://127.0.0.1:8000
```

### Set up the Frontend

Open a second terminal and navigate to the frontend directory:
```bash
cd frontend
```

Install the frontend dependencies:
```bash
npm install
```

Start the React development server:
```bash
npm run dev
```

The frontend will be available at:
```text
http://localhost:5173
```

### Analyze a Project

Open the CodeGuardian dashboard in your browser and enter the path to any accessible Python project directory.

For example:
```text
/Users/yourname/Projects/my-python-project
```

CodeGuardian can analyze projects located inside or outside the CodeGuardian repository.

The dashboard will display:

- Files scanned
- Total issues
- Issues by severity
- Severity breakdown
- Detailed issue results

You can then filter, sort, search, and inspect individual issues directly from the dashboard.


## 💻 CLI Usage

CodeGuardian's command-line interface remains available for terminal-based analysis and automation.

Scan a project:
```bash
python -m codeguardian.main scan path/to/project
```

Generate JSON output:
```bash
python -m codeguardian.main scan path/to/project --json
```

Use a custom configuration:
```bash
python -m codeguardian.main scan path/to/project --config custom.yml
```


## 📷 Dashboard

### Analysis Dashboard

![CodeGuardian Dashboard](assets/dashboard.png)

### Issue Details

![CodeGuardian Issue Details](assets/issue-details.png)


## ⚙️ Configuration

CodeGuardian supports YAML configuration for its static analysis engine.

Example:
```yaml
rules:
  unused_import:
    enabled: true

  dead_code:
    enabled: true

  long_function:
    enabled: true
    max_lines: 75

  too_many_arguments:
    enabled: true
    max_arguments: 6

  circular_dependency:
    enabled: true
```

Configuration settings apply to the underlying analysis engine used by CodeGuardian.


## 🔬 Testing

Run the complete test suite:
```bash
pytest
```

The v1.1.0 release includes a comprehensive automated test suite covering the CodeGuardian analysis engine and backend functionality.

The frontend production build can be verified with:
```bash
cd frontend
npm run build
```


## 🔑 License

This project is licensed under the MIT License. See the `LICENSE` file for details.