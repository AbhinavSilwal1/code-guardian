from fastapi import FastAPI
from backend.app.routes.analysis import router


app = FastAPI(
    title="CodeGuardian API",
)


app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "CodeGuardian API running"
    }