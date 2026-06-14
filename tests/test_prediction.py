from api.prediction import predict_risk


def test_normal_prediction():
    features = {
        "machine_id": "MACHINE_01",
        "temperature": 42,
        "vibration_total": 0.5,
        "rpm": 1450
    }

    result = predict_risk(features)

    assert result["risk_level"] == "NORMAL"
    assert result["failure_probability"] == 0.15


def test_warning_prediction():
    features = {
        "machine_id": "MACHINE_01",
        "temperature": 55,
        "vibration_total": 1.2,
        "rpm": 1450
    }

    result = predict_risk(features)

    assert result["risk_level"] == "WARNING"
    assert result["failure_probability"] == 0.60


def test_critical_prediction():
    features = {
        "machine_id": "MACHINE_01",
        "temperature": 75,
        "vibration_total": 1.9,
        "rpm": 1450
    }

    result = predict_risk(features)

    assert result["risk_level"] == "CRITICAL"
    assert result["failure_probability"] == 0.90