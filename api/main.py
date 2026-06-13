from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from features.feature_extraction import extract_features
from api.prediction import predict_risk
from api.validation import validate_sensor_data


app = FastAPI(title="H2 Predictive Maintenance API")


class SensorData(BaseModel):
    machine_id: str
    temperature: float
    vibration_x: float
    vibration_y: float
    vibration_z: float
    rpm: int


@app.get("/")
def home():
    return {
        "message": "H2 Predictive Maintenance API is running"
    }


@app.post("/predict")
def predict(data: SensorData):
    sensor_data = data.model_dump()

    if not validate_sensor_data(sensor_data):
        raise HTTPException(status_code=400, detail="Invalid sensor data")

    features = extract_features(sensor_data)
    prediction = predict_risk(features)

    return {
        "input": sensor_data,
        "features": features,
        "prediction": prediction
    }