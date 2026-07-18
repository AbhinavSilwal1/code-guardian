from fastapi import FastAPI
from app.routes.analysis import router


app = FastAPI(
    title="CodeGuardian API",
)


app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "CodeGuardian API running"
    }