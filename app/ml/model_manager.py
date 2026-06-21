from ultralytics import YOLO


class ModelManager:

    def __init__(self):

        self.tiger_model = YOLO(
            "models/tiger_detector_v2.pt"
        )

        self.general_model = YOLO(
            "yolov8n.pt"
        )


manager = ModelManager()