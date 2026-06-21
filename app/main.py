from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine
from app.api.v1.cameras import router as camera_router
from app.api.v1.detections import router as detection_router
from app.api.v1.alerts import router as alert_router

app = FastAPI(
    title="Tiger Protection System"
)


@app.get("/")
def root():
    return {"message": "Tiger Protection System Running"}


@app.get("/health/db")
def db_health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))

    return {"database": "connected"}


app.include_router(
    camera_router,
    prefix="/api/v1/cameras",
    tags=["Cameras"]
)

app.include_router(
    detection_router,
    prefix="/api/v1/detections",
    tags=["Detections"]
)

app.include_router(
    alert_router,
    prefix="/api/v1/alerts",
    tags=["Alerts"]
)