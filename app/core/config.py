from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str
    SECRET_KEY: str

    API_V1_PREFIX: str = "/api/v1"

    PROJECT_NAME: str = "Tiger Protection System"

    YOLO_MODEL_PATH: str = "models/yolov8n.pt"

    class Config:
        env_file = ".env"


settings = Settings()
