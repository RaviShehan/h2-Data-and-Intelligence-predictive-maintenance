import json
import os

from fastapi import FastAPI, HTTPException

from api.anomaly import detect_anomaly
from features.feature_extraction import extract_features
from models.predict_real_model import predict_with_real_model
from api.validation import SensorData
from database.db import init_db, save_prediction, get_recent_predictions
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="H2 Predictive Maintenance API",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {
        "message": "H2 Predictive Maintenance API is running"
    }

@app.get("/model-info")
def get_model_info():
    metadata_path = "models/model_metadata_real.json"
    
    if not os.path.exists(metadata_path):
        raise HTTPException(
            status_code=404,
            detail="Real model metadata not found. Run models/train_real_model.py first."        
            )

    with open(metadata_path, "r") as file:
        metadata = json.load(file)

    metadata["model_available"] = os.path.exists(metadata["model_file"])

    return metadata


@app.get("/model-evaluation")
def get_model_evaluation():
    report_path = "models/evaluation_report.json"

    if not os.path.exists(report_path):
        raise HTTPException(
            status_code=404,
            detail="Evaluation report not found. Run models/evaluate_model.py first."
        )

    with open(report_path, "r") as file:
        return json.load(file)


@app.post("/predict")
def predict(data: SensorData):
    sensor_data = data.model_dump()

    if sensor_data["machine_id"].strip() == "":
        raise HTTPException(status_code=422, detail="machine_id cannot be empty")

    if sensor_data["temperature"] < 0 or sensor_data["temperature"] > 120:
        raise HTTPException(status_code=422, detail="temperature must be between 0 and 120")

    if sensor_data["vibration_x"] < 0 or sensor_data["vibration_x"] > 5:
        raise HTTPException(status_code=422, detail="vibration_x must be between 0 and 5")

    if sensor_data["vibration_y"] < 0 or sensor_data["vibration_y"] > 5:
        raise HTTPException(status_code=422, detail="vibration_y must be between 0 and 5")

    if sensor_data["vibration_z"] < 0 or sensor_data["vibration_z"] > 5:
        raise HTTPException(status_code=422, detail="vibration_z must be between 0 and 5")

    if sensor_data["rpm"] < 0 or sensor_data["rpm"] > 10000:
        raise HTTPException(status_code=422, detail="rpm must be between 0 and 10000")

    features = extract_features(sensor_data)
    prediction = predict_with_real_model(features)
    anomaly = detect_anomaly(features)

    prediction_id = save_prediction(sensor_data, features, prediction, anomaly)
    return {
        "prediction_id": prediction_id,
        "input": sensor_data,
        "features": features,
        "prediction": prediction,
        "anomaly_detection": anomaly
    }


@app.get("/predictions")
def predictions():
    return {
        "predictions": get_recent_predictions()
    }