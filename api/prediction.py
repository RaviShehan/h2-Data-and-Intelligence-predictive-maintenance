def predict_risk(features: dict) -> dict:
    temperature = features["temperature"]
    vibration = features["vibration_total"]

    if temperature >= 70 or vibration >= 1.8:
        risk_level = "CRITICAL"
        failure_probability = 0.90
        recommended_action = "Immediate maintenance required"

    elif temperature >= 50 or vibration >= 1.0:
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
        "recommended_action": recommended_action
    }
    