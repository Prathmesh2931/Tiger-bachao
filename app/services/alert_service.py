from app.models.alert import Alert


def create_alert(db, detection_id, threat_score):

    if threat_score < 0.7:
        return None

    severity = "LOW"

    if threat_score > 0.9:
        severity = "CRITICAL"

    elif threat_score > 0.8:
        severity = "HIGH"

    alert = Alert(
        detection_id=detection_id,
        alert_type="Threat Detected",
        severity=severity,
        status="ACTIVE"
    )

    db.add(alert)
    db.commit()
    db.refresh(alert)

    return alert