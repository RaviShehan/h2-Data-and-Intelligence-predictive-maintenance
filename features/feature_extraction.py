import math


def extract_features(data: dict) -> dict:
    vibration_total = math.sqrt(
        data["vibration_x"] ** 2 +
        data["vibration_y"] ** 2 +
        data["vibration_z"] ** 2
    )

    return {
        "machine_id": data["machine_id"],
        "temperature": data["temperature"],
        "vibration_total": round(vibration_total, 3),
        "rpm": data["rpm"]
    }