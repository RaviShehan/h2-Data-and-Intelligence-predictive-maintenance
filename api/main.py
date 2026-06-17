import json
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from api.anomaly import detect_anomaly
from api.validation import SensorData
from database.db import (
    get_connection,
    get_recent_predictions,
    init_db,
    save_prediction,
)
from features.feature_extraction import extract_features
from models.predict_real_model import predict_with_real_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="H2 Predictive Maintenance API",
    lifespan=lifespan,
)


@app.get("/")
def home():
    return {
        "message": "H2 Predictive Maintenance API is running"
    }


@app.get("/system-health")
def get_system_health():
    database_status = "unknown"

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        cursor.fetchone()
        cursor.close()
        connection.close()
        database_status = "connected"
    except Exception:
        database_status = "not_connected"

    model_file_available = os.path.exists("models/trained_model_real.pkl")
    evaluation_report_available = os.path.exists("models/evaluation_report_real.json")
    feature_importance_available = os.path.exists("models/feature_importance_real.json")

    overall_status = "healthy"

    if database_status != "connected":
        overall_status = "degraded"

    if not model_file_available:
        overall_status = "degraded"

    return {
        "system": "H4 Platform Monitoring",
        "overall_status": overall_status,
        "api_status": "running",
        "database_status": database_status,
        "model_file_available": model_file_available,
        "evaluation_report_available": evaluation_report_available,
        "feature_importance_available": feature_importance_available,
    }


@app.get("/model-info")
def get_model_info():
    metadata_path = "models/model_metadata_real.json"

    if not os.path.exists(metadata_path):
        raise HTTPException(
            status_code=404,
            detail="Real model metadata not found. Run models/train_real_model.py first.",
        )

    with open(metadata_path, "r") as file:
        metadata = json.load(file)

    metadata["model_available"] = os.path.exists(metadata["model_file"])

    return metadata


@app.get("/model-evaluation")
def get_model_evaluation():
    report_path = "models/evaluation_report_real.json"

    if not os.path.exists(report_path):
        raise HTTPException(
            status_code=404,
            detail="Evaluation report not found. Run models/evaluate_real_model.py first.",
        )

    with open(report_path, "r") as file:
        return json.load(file)


@app.get("/feature-importance")
def get_feature_importance():
    importance_path = "models/feature_importance_real.json"

    if not os.path.exists(importance_path):
        raise HTTPException(
            status_code=404,
            detail="Feature importance report not found. Run models/feature_importance_real.py first.",
        )

    with open(importance_path, "r") as file:
        return json.load(file)


@app.post("/predict")
def predict(data: SensorData):
    sensor_data = data.model_dump()

    if sensor_data["machine_id"].strip() == "":
        raise HTTPException(
            status_code=422,
            detail="machine_id cannot be empty",
        )

    if sensor_data["temperature"] < 0 or sensor_data["temperature"] > 120:
        raise HTTPException(
            status_code=422,
            detail="temperature must be between 0 and 120",
        )

    if sensor_data["vibration_x"] < 0 or sensor_data["vibration_x"] > 5:
        raise HTTPException(
            status_code=422,
            detail="vibration_x must be between 0 and 5",
        )

    if sensor_data["vibration_y"] < 0 or sensor_data["vibration_y"] > 5:
        raise HTTPException(
            status_code=422,
            detail="vibration_y must be between 0 and 5",
        )

    if sensor_data["vibration_z"] < 0 or sensor_data["vibration_z"] > 5:
        raise HTTPException(
            status_code=422,
            detail="vibration_z must be between 0 and 5",
        )

    if sensor_data["rpm"] < 0 or sensor_data["rpm"] > 10000:
        raise HTTPException(
            status_code=422,
            detail="rpm must be between 0 and 10000",
        )

    features = extract_features(sensor_data)
    prediction = predict_with_real_model(features)
    anomaly = detect_anomaly(features)

    prediction_id = save_prediction(
        sensor_data,
        features,
        prediction,
        anomaly,
    )

    return {
        "prediction_id": prediction_id,
        "input": sensor_data,
        "features": features,
        "prediction": prediction,
        "anomaly_detection": anomaly,
    }


@app.get("/predictions")
def predictions():
    return {
        "predictions": get_recent_predictions()
    }
