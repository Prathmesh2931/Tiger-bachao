from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

from app.models import Base


class Alert(Base):

    __tablename__ = "alerts"

    alert_id = Column(Integer, primary_key=True, index=True)

    detection_id = Column(
        Integer,
        ForeignKey("detections.detection_id")
    )

    alert_type = Column(String)

    severity = Column(String)

    status = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
