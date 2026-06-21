from pydantic import BaseModel


class CameraCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    zone_type: str
    status: str


class CameraResponse(CameraCreate):
    camera_id: int

    class Config:
        from_attributes = True
