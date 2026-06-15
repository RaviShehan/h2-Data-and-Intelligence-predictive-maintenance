import os

import pandas as pd


DATA_PATH = "data/training_data_real.csv"


def test_real_training_dataset_exists():
    assert os.path.exists(DATA_PATH)


def test_real_training_dataset_has_required_columns():
    df = pd.read_csv(DATA_PATH)

    required_columns = [
        "source_file",
        "temperature",
        "rpm",
        "vibration_total",
        "vibration_rms",
        "vibration_mean",
        "vibration_peak",
        "vibration_std",
        "risk_level"
    ]

    for column in required_columns:
        assert column in df.columns


def test_real_training_dataset_has_risk_classes():
    df = pd.read_csv(DATA_PATH)

    risk_classes = set(df["risk_level"].unique())

    assert "NORMAL" in risk_classes
    assert "WARNING" in risk_classes
    assert "CRITICAL" in risk_classes


def test_real_training_dataset_not_empty():
    df = pd.read_csv(DATA_PATH)

    assert len(df) > 0