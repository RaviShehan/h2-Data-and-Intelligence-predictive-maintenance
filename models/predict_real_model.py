import os

import joblib
import pandas as pd


MODEL_PATH = "models/trained_model_real.pkl"


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


def load_real_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "Real trained model not found. Run models/train_real_model.py first."
        )

    return joblib.load(MODEL_PATH)


def predict_with_real_model(features: dict) -> dict:
    model = load_real_model()

    input_data = pd.DataFrame([{
        column: features[column]
        for column in FEATURE_COLUMNS
    }])

    risk_level = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]
    class_labels = model.classes_

    probability_map = {
        class_labels[i]: round(float(probabilities[i]), 2)
        for i in range(len(class_labels))
    }

    failure_probability = probability_map.get(risk_level, 0.0)

    if risk_level == "CRITICAL":
        recommended_action = "Immediate maintenance required"
    elif risk_level == "WARNING":
        recommended_action = "Schedule inspection soon"
    else:
        recommended_action = "Machine operating normally"

    return {
        "machine_id": features["machine_id"],
        "risk_level": risk_level,
        "failure_probability": failure_probability,
        "recommended_action": recommended_action,
        "model_type": "RandomForestClassifier",
        "dataset_source": "NASA IMS Bearing Dataset",
        "probabilities": probability_map
    }

