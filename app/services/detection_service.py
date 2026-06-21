from app.ml.yolo_detector import (
    detect_tiger,
    detect_general
)

from app.models.detection import Detection

from app.services.threat_scoring import (
    calculate_threat
)

from app.services.alert_service import (
    create_alert
)


def process_image(
    db,
    image_path,
    camera_id=1
):

    detections = []

    detections.extend(
        detect_tiger(image_path)
    )

    detections.extend(
        detect_general(image_path)
    )

    saved = []

    for d in detections:

        threat = calculate_threat(d)

        det = Detection(
            camera_id=camera_id,
            species=d["class"],
            confidence=d["confidence"],
            image_path=image_path,
            bbox_coords=str(d["bbox"]),
            threat_score=threat
        )

        db.add(det)
        db.commit()
        db.refresh(det)

        create_alert(
            db,
            det.detection_id,
            threat
        )

        saved.append(det)

    return saved