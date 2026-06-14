from features.feature_extraction import extract_features


def test_extract_features_for_high_temperature_data():
    sensor_data = {
        "machine_id": "MACHINE_01",
        "temperature": 75,
        "vibration_x": 1.2,
        "vibration_y": 1.0,
        "vibration_z": 1.1,
        "rpm": 1450
    }

    features = extract_features(sensor_data)

    assert features["machine_id"] == "MACHINE_01"
    assert features["temperature"] == 75
    assert features["temperature_status"] == "HIGH"
    assert features["vibration_total"] == 1.91
    assert features["vibration_rms"] == 1.103
    assert features["vibration_mean"] == 1.1
    assert features["vibration_peak"] == 1.2
    assert features["vibration_std"] == 0.082
    assert features["rpm"] == 1450


def test_extract_features_for_normal_temperature_data():
    sensor_data = {
        "machine_id": "MACHINE_02",
        "temperature": 45,
        "vibration_x": 0.2,
        "vibration_y": 0.3,
        "vibration_z": 0.4,
        "rpm": 1450
    }

    features = extract_features(sensor_data)

    assert features["temperature_status"] == "NORMAL"
    assert features["vibration_total"] == 0.539