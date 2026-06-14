import math
import numpy as np


def extract_features(data: dict) -> dict:
    vibration_values = np.array([
        data["vibration_x"],
        data["vibration_y"],
        data["vibration_z"]
    ])

    vibration_total = math.sqrt(
        data["vibration_x"] ** 2 +
        data["vibration_y"] ** 2 +
        data["vibration_z"] ** 2
    )

    vibration_rms = math.sqrt(np.mean(vibration_values ** 2))
    vibration_mean = np.mean(vibration_values)
    vibration_peak = np.max(vibration_values)
    vibration_std = np.std(vibration_values)

    temperature = data["temperature"]

    if temperature >= 70:
        temperature_status = "HIGH"
    elif temperature >= 50:
        temperature_status = "ELEVATED"
    else:
        temperature_status = "NORMAL"

    return {
        "machine_id": data["machine_id"],
        "temperature": temperature,
        "temperature_status": temperature_status,
        "vibration_total": round(vibration_total, 3),
        "vibration_rms": round(vibration_rms, 3),
        "vibration_mean": round(float(vibration_mean), 3),
        "vibration_peak": round(float(vibration_peak), 3),
        "vibration_std": round(float(vibration_std), 3),
        "rpm": data["rpm"]
    }