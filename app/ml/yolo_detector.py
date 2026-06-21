from ultralytics import YOLO

tiger_model = YOLO(
    "runs/detect/runs/detect/tiger_detector_v2/weights/best.pt"
)

general_model = YOLO("yolov8n.pt")


def detect_tiger(image_path):

    results = tiger_model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            detections.append(
                {
                    "class": "Tiger",
                    "confidence": float(box.conf[0]),
                    "bbox": [x1, y1, x2, y2]
                }
            )

    return detections


def detect_general(image_path):

    results = general_model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            detections.append(
                {
                    "class": general_model.names[cls],
                    "confidence": float(box.conf[0]),
                    "bbox": [x1, y1, x2, y2]
                }
            )

    return detections