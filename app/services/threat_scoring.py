def calculate_threat(detection):

    cls = detection["class"]

    if cls == "Tiger":
        return 0.95

    if cls == "person":
        return 0.85

    if cls in ["truck", "car", "bus", "motorcycle"]:
        return 0.75

    return 0.2