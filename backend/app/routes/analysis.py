from fastapi import APIRouter
from app.services.guardian_service import analyze_project


router = APIRouter(
    prefix="/api",
    tags=["Analysis"],
)


@router.post("/analyze")
def analyze(path: str):
    return analyze_project(path)