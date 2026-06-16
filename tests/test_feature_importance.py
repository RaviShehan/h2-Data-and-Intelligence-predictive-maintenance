import os
import json


FEATURE_IMPORTANCE_PATH = "models/feature_importance_real.json"


def test_feature_importance_file_exists():
    assert os.path.exists(FEATURE_IMPORTANCE_PATH)


def test_feature_importance_file_has_required_keys():
    with open(FEATURE_IMPORTANCE_PATH, "r") as file:
        data = json.load(file)

    assert data["model_type"] == "RandomForestClassifier"
    assert data["dataset_source"] == "NASA IMS Bearing Dataset"
    assert "feature_importance" in data


def test_feature_importance_contains_values():
    with open(FEATURE_IMPORTANCE_PATH, "r") as file:
        data = json.load(file)

    feature_importance = data["feature_importance"]

    assert len(feature_importance) > 0
    assert "feature" in feature_importance[0]
    assert "importance" in feature_importance[0]


def test_feature_importance_contains_scipy_features():
    with open(FEATURE_IMPORTANCE_PATH, "r") as file:
        data = json.load(file)

    features = [
        item["feature"]
        for item in data["feature_importance"]
    ]

    assert "signal_skewness" in features
    assert "signal_kurtosis" in features
    assert "spectral_energy" in features