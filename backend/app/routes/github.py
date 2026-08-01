from fastapi import APIRouter, HTTPException
from git.exc import GitCommandError

from backend.app.services.github.github_service import (
    GitHubService,
)


router = APIRouter()

service = GitHubService()


@router.post("/github/analyze")
def analyze_github_repository(url: str):
    try:
        return service.analyze_repository(url)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    except GitCommandError as exc:

        error_message = str(exc).lower()

        if "repository not found" in error_message:
            detail = (
                "Repository not found. "
                "Please verify the GitHub URL."
            )

        elif "authentication failed" in error_message:
            detail = (
                "Unable to access the repository. "
                "It may be private."
            )

        else:
            detail = (
                "Unable to clone the GitHub repository."
            )

        raise HTTPException(
            status_code=400,
            detail=detail,
        ) from exc