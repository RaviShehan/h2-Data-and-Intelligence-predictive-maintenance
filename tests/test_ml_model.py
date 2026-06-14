from models.predict_model import predict_with_model


def test_ml_model_predicts_critical():
    features = {
        "machine_id": "MACHINE_01",
        "temperature": 75,
        "vibration_total": 1.91,
        "rpm": 1450
    }

    result = predict_with_model(features)

    assert result["risk_level"] == "CRITICAL"
    assert result["model_type"] == "RandomForestClassifier"
    assert "probabilities" in result