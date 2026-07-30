from fastapi import APIRouter, HTTPException
from backend.app.services.github.github_service import (
    GitHubService,
)


router = APIRouter()

service = GitHubService()


@router.post("/github/analyze")
def analyze_github_repository(url: str,):
    try:
        return service.analyze_repository(url)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )