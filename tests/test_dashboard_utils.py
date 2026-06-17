from dashboard.dashboard_utils import normalize_predictions


def test_normalize_predictions_from_dictionary_response():
    response = {
        "predictions": [
            {
                "machine_id": "EDGE_MACHINE_01",
                "risk_level": "NORMAL"
            }
        ]
    }

    result = normalize_predictions(response)

    assert len(result) == 1
    assert result[0]["machine_id"] == "EDGE_MACHINE_01"
    assert result[0]["risk_level"] == "NORMAL"


def test_normalize_predictions_from_list_response():
    response = [
        {
            "machine_id": "EDGE_MACHINE_02",
            "risk_level": "CRITICAL"
        }
    ]

    result = normalize_predictions(response)

    assert len(result) == 1
    assert result[0]["machine_id"] == "EDGE_MACHINE_02"
    assert result[0]["risk_level"] == "CRITICAL"


def test_normalize_predictions_from_json_string_response():
    response = {
        "predictions": [
            '{"machine_id": "EDGE_MACHINE_03", "risk_level": "WARNING"}'
        ]
    }

    result = normalize_predictions(response)

    assert len(result) == 1
    assert result[0]["machine_id"] == "EDGE_MACHINE_03"
    assert result[0]["risk_level"] == "WARNING"


def test_normalize_predictions_ignores_invalid_json_string():
    response = {
        "predictions": [
            "invalid-json"
        ]
    }

    result = normalize_predictions(response)

    assert result == []
