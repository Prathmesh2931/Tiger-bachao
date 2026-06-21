from pydantic import BaseModel


class AlertCreate(BaseModel):

    detection_id: int
    alert_type: str
    severity: str
    status: str
