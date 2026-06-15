from features.signal_processing import extract_signal_features
from models.predict_real_model import predict_with_real_model


def test_real_nasa_model_prediction():
    vibration_values = [1.2, 1.0, 1.1]

    signal_features = extract_signal_features(vibration_values)

    features = {
        "machine_id": "MACHINE_01",
        "vibration_total": 1.91,
        "vibration_rms": 1.103,
        "vibration_mean": 1.1,
        "vibration_peak": 1.2,
        "vibration_std": 0.082,
        **signal_features
    }

    result = predict_with_real_model(features)

    assert result["model_type"] == "RandomForestClassifier"
    assert result["dataset_source"] == "NASA IMS Bearing Dataset"
    assert result["risk_level"] in ["NORMAL", "WARNING", "CRITICAL"]
    assert "failure_probability" in result
    assert "probabilities" in result