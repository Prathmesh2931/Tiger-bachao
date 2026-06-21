from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.models import Base


class Camera(Base):
    __tablename__ = "cameras"

    camera_id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    latitude = Column(Float)

    longitude = Column(Float)

    zone_type = Column(String)

    status = Column(String)
