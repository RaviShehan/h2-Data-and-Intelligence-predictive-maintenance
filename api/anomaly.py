def detect_anomaly(features: dict) -> dict:
    anomaly_reasons = []

    temperature = features["temperature"]
    vibration_total = features["vibration_total"]
    rpm = features["rpm"]

    if temperature >= 80:
        anomaly_reasons.append("Very high temperature detected")

    if vibration_total >= 2.0:
        anomaly_reasons.append("Abnormal vibration level detected")

    if rpm < 500:
        anomaly_reasons.append("RPM too low for normal operation")

    if rpm > 5000:
        anomaly_reasons.append("RPM too high for normal operation")

    is_anomaly = len(anomaly_reasons) > 0

    return {
        "is_anomaly": is_anomaly,
        "anomaly_reasons": anomaly_reasons
    }