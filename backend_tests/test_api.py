from fastapi.testclient import TestClient
from backend.app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "CodeGuardian API running"
    }


def test_analyze_endpoint():
    response = client.post(
        "/api/analyze",
        params={
            "path": "examples/sample_project"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert "issues" in data


def test_analyze_response_structure():
    response = client.post(
        "/api/analyze",
        params={
            "path": "examples/sample_project"
        },
    )

    data = response.json()

    summary = data["summary"]

    assert "files_scanned" in summary
    assert "total_issues" in summary
    assert "severity_counts" in summary
    assert "category_counts" in summary