from app.core.database import SessionLocal
from app.services.detection_service import process_image

db = SessionLocal()

result = process_image(
    db=db,
    image_path="test_images/per_vehicle.png",
    camera_id=1
)

print(result)
