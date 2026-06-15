import json

import joblib
import pandas as pd


MODEL_PATH = "models/trained_model_real.pkl"
OUTPUT_PATH = "models/feature_importance_real.json"

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


def generate_feature_importance():
    model = joblib.load(MODEL_PATH)

    importances = model.feature_importances_

    importance_data = []

    for feature, importance in zip(FEATURE_COLUMNS, importances):
        importance_data.append({
            "feature": feature,
            "importance": round(float(importance), 6)
        })

    importance_data = sorted(
        importance_data,
        key=lambda item: item["importance"],
        reverse=True
    )

    result = {
        "model_type": "RandomForestClassifier",
        "dataset_source": "NASA IMS Bearing Dataset",
        "feature_importance": importance_data
    }

    with open(OUTPUT_PATH, "w") as file:
        json.dump(result, file, indent=4)

    print("Feature importance report generated")
    print(f"Saved to: {OUTPUT_PATH}")
    print()

    df = pd.DataFrame(importance_data)
    print(df)


if __name__ == "__main__":
    generate_feature_importance()