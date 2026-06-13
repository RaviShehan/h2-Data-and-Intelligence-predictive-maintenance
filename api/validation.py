def validate_sensor_data(data: dict) -> bool:
    required_fields = [
        "machine_id",
        "temperature",
        "vibration_x",
        "vibration_y",
        "vibration_z",
        "rpm"
    ]

    for field in required_fields:
        if field not in data:
            return False

    if data["temperature"] < -20 or data["temperature"] > 150:
        return False

    if data["rpm"] < 0:
        return False

    return True