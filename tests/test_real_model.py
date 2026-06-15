from models.predict_real_model import predict_with_real_model


def test_real_nasa_model_prediction():
    features = {
        "machine_id": "MACHINE_01",
        "vibration_total": 1.91,
        "vibration_rms": 1.103,
        "vibration_mean": 1.1,
        "vibration_peak": 1.2,
        "vibration_std": 0.082
    }

    result = predict_with_real_model(features)

    assert result["model_type"] == "RandomForestClassifier"
    assert result["dataset_source"] == "NASA IMS Bearing Dataset"
    assert result["risk_level"] in ["NORMAL", "WARNING", "CRITICAL"]
    assert "failure_probability" in result
    assert "probabilities" in result