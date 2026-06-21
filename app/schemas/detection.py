from pydantic import BaseModel


class DetectionCreate(BaseModel):

    camera_id: int

    species: str

    confidence: float

    image_path: str

    bbox_coords: str

    threat_score: float


class DetectionResponse(DetectionCreate):

    detection_id: int

    class Config:
        from_attributes = True
