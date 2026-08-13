from fastapi.testclient import TestClient
from backend.app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert "CodeGuardian" in response.text


def test_analyze_endpoint(tmp_path):
    project = tmp_path / "sample_project"

    project.mkdir()

    (project / "app.py").write_text(
        """
import os

def hello():
    print("Hello World")
"""
    )

    response = client.post(
        "/api/analyze",
        params={
            "path": str(project)
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert "issues" in data


def test_analyze_response_structure(tmp_path):
    project = tmp_path / "sample_project"

    project.mkdir()

    (project / "app.py").write_text(
        """
import os

def hello():
    print("Hello World")
"""
    )

    response = client.post(
        "/api/analyze",
        params={
            "path": str(project)
        },
    )

    assert response.status_code == 200

    data = response.json()

    summary = data["summary"]

    assert "files_scanned" in summary
    assert "total_issues" in summary
    assert "severity_counts" in summary
    assert "category_counts" in summary