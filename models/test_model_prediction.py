from models.predict_model import predict_with_model


features = {
    "machine_id": "MACHINE_01",
    "temperature": 75,
    "vibration_total": 1.91,
    "rpm": 1450
}

result = predict_with_model(features)

print(result)