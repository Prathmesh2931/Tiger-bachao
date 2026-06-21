from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

from app.models import Base


class Detection(Base):

    __tablename__ = "detections"

    detection_id = Column(Integer, primary_key=True, index=True)

    camera_id = Column(
        Integer,
        ForeignKey("cameras.camera_id")
    )

    species = Column(String)

    confidence = Column(Float)

    image_path = Column(String)

    bbox_coords = Column(String)

    threat_score = Column(Float)

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
