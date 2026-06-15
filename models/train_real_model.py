import os
import json
from datetime import datetime

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib


DATA_PATH = "data/training_data_real.csv"
MODEL_PATH = "models/trained_model_real.pkl"
METADATA_PATH = "models/model_metadata_real.json"


FEATURE_COLUMNS = [
    "vibration_total",
    "vibration_rms",
    "vibration_mean",
    "vibration_peak",
    "vibration_std",
    "signal_rms",
    "signal_mean",
    "signal_peak",
    "signal_std",
    "signal_skewness",
    "signal_kurtosis",
    "spectral_energy"
]


def train_real_model():
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURE_COLUMNS]
    y = df["risk_level"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Real NASA IMS model training completed with SciPy signal features")
    print("Accuracy:", round(accuracy, 4))
    print(classification_report(y_test, predictions))

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, MODEL_PATH)
    print(f"Real model saved to {MODEL_PATH}")

    metadata = {
        "model_name": "NASA IMS Bearing Risk Prediction Model",
        "model_type": "RandomForestClassifier",
        "model_file": MODEL_PATH,
        "training_data": DATA_PATH,
        "trained_at": datetime.now().isoformat(),
        "dataset_source": "NASA IMS Bearing Dataset",
        "input_features": FEATURE_COLUMNS,
        "risk_classes": [
            "NORMAL",
            "WARNING",
            "CRITICAL"
        ],
        "accuracy": round(float(accuracy), 4)
    }

    with open(METADATA_PATH, "w") as file:
        json.dump(metadata, file, indent=4)

    print(f"Real model metadata saved to {METADATA_PATH}")


if __name__ == "__main__":
    train_real_model()