from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("test_images/tiger.jpg")

for r in results:
    print(r.names)
