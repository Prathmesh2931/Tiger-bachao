from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.services.detection_service import (
    process_image
)

router = APIRouter()


@router.post("/process")

def process(
    image_path: str,
    db: Session = Depends(get_db)
):

    results = process_image(
        db,
        image_path
    )

    return {
        "detections": len(results)
    }