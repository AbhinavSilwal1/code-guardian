from fastapi import APIRouter
from backend.app.schemas.analysis import AnalysisResponse
from backend.app.services.guardian_service import analyze_project


router = APIRouter(
    prefix="/api",
    tags=["Analysis"],
)


@router.post(
    "/analyze",
    response_model=AnalysisResponse,
)
def analyze(path: str):
    return analyze_project(path)