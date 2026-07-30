import pytest
from backend.app.services.github.github_client import (
    GitHubClient,
)


def test_parse_repository_url():
    client = GitHubClient()

    result = client.parse_repository_url("https://github.com/user/project")

    assert result == {
        "owner": "user",
        "repository": "project",
    }


def test_parse_invalid_repository_url():
    client = GitHubClient()

    with pytest.raises(ValueError):
        client.parse_repository_url(
            "https://example.com/user/project"
        )