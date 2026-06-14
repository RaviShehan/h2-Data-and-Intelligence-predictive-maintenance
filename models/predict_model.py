import os
import joblib
import pandas as pd


MODEL_PATH = "models/trained_model.pkl"


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "Trained model not found. Run models/train_model.py first."
        )

    return joblib.load(MODEL_PATH)


def predict_with_model(features: dict) -> dict:
    model = load_model()

    input_data = pd.DataFrame([{
        "temperature": features["temperature"],
        "vibration_total": features["vibration_total"],
        "rpm": features["rpm"]
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
        "probabilities": probability_map
    }