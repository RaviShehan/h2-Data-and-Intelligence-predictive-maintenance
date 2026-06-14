import json
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


DATA_PATH = "data/training_data.csv"
MODEL_PATH = "models/trained_model.pkl"
REPORT_PATH = "models/evaluation_report.json"


def evaluate_model():
    df = pd.read_csv(DATA_PATH)

    X = df[["temperature", "vibration_total", "rpm"]]
    y = df["risk_level"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = joblib.load(MODEL_PATH)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)
    matrix = confusion_matrix(y_test, predictions)

    evaluation_result = {
        "model_type": "RandomForestClassifier",
        "dataset": DATA_PATH,
        "model_file": MODEL_PATH,
        "input_features": [
            "temperature",
            "vibration_total",
            "rpm"
        ],
        "risk_classes": [
            "NORMAL",
            "WARNING",
            "CRITICAL"
        ],
        "accuracy": round(float(accuracy), 4),
        "classification_report": report,
        "confusion_matrix": matrix.tolist()
    }

    with open(REPORT_PATH, "w") as file:
        json.dump(evaluation_result, file, indent=4)

    print("Model Evaluation Report")
    print("-----------------------")
    print("Accuracy:", round(accuracy, 4))
    print()
    print("Classification Report:")
    print(classification_report(y_test, predictions))
    print("Confusion Matrix:")
    print(matrix)
    print()
    print(f"Evaluation report saved to {REPORT_PATH}")


if __name__ == "__main__":
    evaluate_model()