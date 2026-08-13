from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.app.routes.analysis import router
from backend.app.routes.github import router as github_router


app = FastAPI(title="CodeGuardian API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    router,
    prefix="/api",
)


app.include_router(
    github_router,
    prefix="/api",
)


frontend_dist = Path("frontend/dist")


if frontend_dist.exists():
    app.mount(
        "/",
        StaticFiles(
            directory=frontend_dist,
            html=True,
        ),
        name="frontend",
    )

else:
    @app.get("/")
    def root():
        return {"message": "CodeGuardian API running"}