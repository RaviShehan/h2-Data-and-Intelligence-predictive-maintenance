import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from features.feature_extraction import extract_features
from models.predict_model import predict_with_model
from api.validation import SensorData
from database.db import init_db, save_prediction, get_recent_predictions


app = FastAPI(title="H2 Predictive Maintenance API")


class SensorData(BaseModel):
    machine_id: str
    temperature: float
    vibration_x: float
    vibration_y: float
    vibration_z: float
    rpm: int


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
def home():
    return {
        "message": "H2 Predictive Maintenance API is running"
    }

@app.get("/model-info")
def get_model_info():
    model_path = "models/trained_model.pkl"

    return {
        "model_name": "Machine Health Risk Prediction Model",
        "model_type": "RandomForestClassifier",
        "model_file": model_path,
        "model_available": os.path.exists(model_path),
        "input_features": [
            "temperature",
            "vibration_total",
            "rpm"
        ],
        "risk_classes": [
            "NORMAL",
            "WARNING",
            "CRITICAL"
        ],
        "output": {
            "risk_level": "Predicted machine health risk",
            "failure_probability": "Probability of predicted risk class",
            "probabilities": "Probability values for each class"
        },
        "purpose": "Predict machine failure risk using extracted sensor features"
    }


@app.post("/predict")
def predict(data: SensorData):
    sensor_data = data.model_dump()

    features = extract_features(sensor_data)
    prediction = predict_with_model(features)

    prediction_id = save_prediction(sensor_data, features, prediction)

    return {
        "prediction_id": prediction_id,
        "input": sensor_data,
        "features": features,
        "prediction": prediction
    }


@app.get("/predictions")
def predictions():
    return {
        "predictions": get_recent_predictions()
    }