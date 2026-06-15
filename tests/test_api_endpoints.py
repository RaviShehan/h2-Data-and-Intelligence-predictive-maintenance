from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


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

def test_model_evaluation_endpoint():
    response = client.get("/model-evaluation")

    assert response.status_code == 200

    data = response.json()

    assert data["model_type"] == "RandomForestClassifier"
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