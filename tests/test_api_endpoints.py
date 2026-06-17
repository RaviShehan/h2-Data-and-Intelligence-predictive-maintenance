from fastapi.testclient import TestClient
from api.main import app
from database.db import init_db

client = TestClient(app)
init_db()

def test_health_check_endpoint():
    response = client.get("/")

    assert response.status_code == 200


def test_model_info_endpoint():
    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()

    assert data["model_type"] == "RandomForestClassifier"
    assert data["dataset_source"] == "NASA IMS Bearing Dataset"
    assert data["model_available"] is True
    assert "vibration_total" in data["input_features"]
    assert "vibration_rms" in data["input_features"]
    assert "vibration_mean" in data["input_features"]
    assert "vibration_peak" in data["input_features"]
    assert "vibration_std" in data["input_features"]
    assert "signal_rms" in data["input_features"]
    assert "signal_mean" in data["input_features"]
    assert "signal_peak" in data["input_features"]
    assert "signal_std" in data["input_features"]
    assert "signal_skewness" in data["input_features"]
    assert "signal_kurtosis" in data["input_features"]
    assert "spectral_energy" in data["input_features"]

def test_model_evaluation_endpoint():
    response = client.get("/model-evaluation")

    assert response.status_code == 200

    data = response.json()

    assert data["model_type"] == "RandomForestClassifier"
    assert data["dataset_source"] == "NASA IMS Bearing Dataset"
    assert data["dataset"] == "data/training_data_real.csv"
    assert data["model_file"] == "models/trained_model_real.pkl"
    assert "accuracy" in data
    assert "classification_report" in data
    assert "confusion_matrix" in data   


def test_predict_rejects_invalid_sensor_data():
    invalid_data = {
        "machine_id": "",
        "temperature": -10,
        "vibration_x": 20,
        "vibration_y": 1.0,
        "vibration_z": 1.1,
        "rpm": -100
    }

    response = client.post("/predict", json=invalid_data)

    assert response.status_code == 422

def test_predict_endpoint_uses_real_nasa_model():
    sensor_data = {
        "machine_id": "MACHINE_01",
        "temperature": 75,
        "vibration_x": 1.2,
        "vibration_y": 1.0,
        "vibration_z": 1.1,
        "rpm": 1450
    }

    response = client.post("/predict", json=sensor_data)

    assert response.status_code == 200

    data = response.json()

    assert "prediction_id" in data
    assert "features" in data
    assert "signal_rms" in data["features"]
    assert "signal_mean" in data["features"]
    assert "signal_peak" in data["features"]
    assert "signal_std" in data["features"]
    assert "signal_skewness" in data["features"]
    assert "signal_kurtosis" in data["features"]
    assert "spectral_energy" in data["features"]
    assert "prediction" in data
    assert "anomaly_detection" in data

    assert data["prediction"]["model_type"] == "RandomForestClassifier"
    assert data["prediction"]["dataset_source"] == "NASA IMS Bearing Dataset"
    assert data["prediction"]["risk_level"] in ["NORMAL", "WARNING", "CRITICAL"]
    assert "probabilities" in data["prediction"]


def test_feature_importance_endpoint():
    response = client.get("/feature-importance")

    assert response.status_code == 200

    data = response.json()

    assert data["model_type"] == "RandomForestClassifier"
    assert data["dataset_source"] == "NASA IMS Bearing Dataset"
    assert "feature_importance" in data
    assert len(data["feature_importance"]) > 0
