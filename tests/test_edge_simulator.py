from edge.edge_device_simulator import (
    apply_edge_filtering,
    generate_raw_sensor_data,
    validate_telemetry,
)


def test_generate_raw_sensor_data_has_required_fields():
    data = generate_raw_sensor_data("EDGE_MACHINE_01")

    assert data["machine_id"] == "EDGE_MACHINE_01"
    assert "temperature" in data
    assert "vibration_x" in data
    assert "vibration_y" in data
    assert "vibration_z" in data
    assert "rpm" in data
    assert "timestamp" in data


def test_apply_edge_filtering_rounds_sensor_values():
    raw_data = {
        "machine_id": "EDGE_MACHINE_01",
        "temperature": 45.678,
        "vibration_x": 1.234,
        "vibration_y": 2.345,
        "vibration_z": 3.456,
        "rpm": 1500,
        "timestamp": "2026-06-17T10:00:00"
    }

    filtered_data = apply_edge_filtering(raw_data)

    assert filtered_data["temperature"] == 45.7
    assert filtered_data["vibration_x"] == 1.23
    assert filtered_data["vibration_y"] == 2.35
    assert filtered_data["vibration_z"] == 3.46
    assert filtered_data["rpm"] == 1500


def test_validate_telemetry_accepts_valid_data():
    valid_data = {
        "machine_id": "EDGE_MACHINE_01",
        "temperature": 60,
        "vibration_x": 1.0,
        "vibration_y": 1.2,
        "vibration_z": 0.8,
        "rpm": 1500,
        "timestamp": "2026-06-17T10:00:00"
    }

    assert validate_telemetry(valid_data) is True


def test_validate_telemetry_rejects_invalid_data():
    invalid_data = {
        "machine_id": "",
        "temperature": 150,
        "vibration_x": 6,
        "vibration_y": 1.2,
        "vibration_z": 0.8,
        "rpm": 15000,
        "timestamp": "2026-06-17T10:00:00"
    }

    assert validate_telemetry(invalid_data) is False