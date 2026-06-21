from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.camera import Camera
from app.schemas.camera import CameraCreate

router = APIRouter()


@router.post("/")
def create_camera(
    camera: CameraCreate,
    db: Session = Depends(get_db)
):
    db_camera = Camera(
        name=camera.name,
        latitude=camera.latitude,
        longitude=camera.longitude,
        zone_type=camera.zone_type,
        status=camera.status
    )

    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)

    return db_camera


@router.get("/")
def get_cameras(
    db: Session = Depends(get_db)
):
    return db.query(Camera).all()
