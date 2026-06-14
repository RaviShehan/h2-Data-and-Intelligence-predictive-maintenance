from api.anomaly import detect_anomaly


def test_detects_temperature_anomaly():
    features = {
        "temperature": 85,
        "vibration_total": 1.2,
        "rpm": 1450
    }

    result = detect_anomaly(features)

    assert result["is_anomaly"] is True
    assert "Very high temperature detected" in result["anomaly_reasons"]


def test_detects_vibration_anomaly():
    features = {
        "temperature": 60,
        "vibration_total": 2.2,
        "rpm": 1450
    }

    result = detect_anomaly(features)

    assert result["is_anomaly"] is True
    assert "Abnormal vibration level detected" in result["anomaly_reasons"]


def test_normal_data_has_no_anomaly():
    features = {
        "temperature": 45,
        "vibration_total": 0.6,
        "rpm": 1450
    }

    result = detect_anomaly(features)

    assert result["is_anomaly"] is False
    assert result["anomaly_reasons"] == []