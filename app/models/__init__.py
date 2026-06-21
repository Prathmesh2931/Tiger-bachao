from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models so SQLAlchemy registers tables
from app.models.camera import Camera
from app.models.detection import Detection
from app.models.alert import Alert
from app.models.tiger import *
from app.models.railway import *
from app.models.village import *
from app.models.user import *