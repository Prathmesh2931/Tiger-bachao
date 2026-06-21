from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.models.alert import Alert

from app.schemas.alert import AlertCreate

router = APIRouter()


@router.post("/")
def create_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db)
):

    db_alert = Alert(**alert.model_dump())

    db.add(db_alert)

    db.commit()

    db.refresh(db_alert)

    return db_alert


@router.get("/")
def get_alerts(
    db: Session = Depends(get_db)
):

    return db.query(Alert).all()
