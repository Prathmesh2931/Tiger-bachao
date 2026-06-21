from app.models import Base

from app.core.database import engine

import app.models.camera
import app.models.alert
import app.models.detection

Base.metadata.create_all(bind=engine)

print("Tables Created")
