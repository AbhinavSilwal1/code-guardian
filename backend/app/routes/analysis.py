from fastapi import APIRouter, HTTPException
from backend.app.services.guardian_service import analyze_project


router = APIRouter()


@router.post("/analyze")
def analyze(path: str):

    try:
        return analyze_project(path)

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc