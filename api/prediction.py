def predict_risk(features: dict) -> dict:
    temperature = features["temperature"]
    vibration_total = features["vibration_total"]
    vibration_rms = features.get("vibration_rms", vibration_total)

    risk_score = 0

    if temperature >= 70:
        risk_score += 2
    elif temperature >= 50:
        risk_score += 1

    if vibration_total >= 1.8:
        risk_score += 2
    elif vibration_total >= 1.0:
        risk_score += 1

    if vibration_rms >= 1.0:
        risk_score += 1

    if risk_score >= 3:
        risk_level = "CRITICAL"
        failure_probability = 0.90
        recommended_action = "Immediate maintenance required"

    elif risk_score >= 1:
        risk_level = "WARNING"
        failure_probability = 0.60
        recommended_action = "Schedule inspection soon"

    else:
        risk_level = "NORMAL"
        failure_probability = 0.15
        recommended_action = "Machine operating normally"

    return {
        "machine_id": features["machine_id"],
        "risk_level": risk_level,
        "failure_probability": failure_probability,
        "recommended_action": recommended_action,
        "risk_score": risk_score
    }