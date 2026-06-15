from models.predict_real_model import predict_with_real_model


features = {
    "machine_id": "MACHINE_01",
    "vibration_total": 1.91,
    "vibration_rms": 1.103,
    "vibration_mean": 1.1,
    "vibration_peak": 1.2,
    "vibration_std": 0.082
}

result = predict_with_real_model(features)
print(result)