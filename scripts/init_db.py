from app.models.detection import Detection
from app.core.database import engine

from app.models import Base
from app.models.camera import Camera
from app.models.alert import Alert

Base.metadata.create_all(bind=engine)

print("Database tables created successfully")
