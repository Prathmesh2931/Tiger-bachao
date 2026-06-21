from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="training/datasets/Wild-animal-detection-1/data.yaml",
    epochs=30,
    imgsz=640,
    batch=8,
    workers=4,
    device="cpu",
    name="tiger_lion_detector"
)
