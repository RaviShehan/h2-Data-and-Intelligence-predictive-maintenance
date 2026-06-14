import os
import random
import math
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib


MODEL_PATH = "models/trained_model.pkl"
DATA_PATH = "data/training_data.csv"


def calculate_vibration_total(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)


def generate_training_data():
    rows = []

    for _ in range(120):
        temperature = random.uniform(35, 49)
        vibration_x = random.uniform(0.1, 0.4)
        vibration_y = random.uniform(0.1, 0.4)
        vibration_z = random.uniform(0.1, 0.4)
        vibration_total = calculate_vibration_total(vibration_x, vibration_y, vibration_z)

        rows.append({
            "temperature": round(temperature, 2),
            "vibration_total": round(vibration_total, 3),
            "rpm": 1450,
            "risk_level": "NORMAL"
        })

    for _ in range(120):
        temperature = random.uniform(50, 69)
        vibration_x = random.uniform(0.4, 0.8)
        vibration_y = random.uniform(0.4, 0.8)
        vibration_z = random.uniform(0.4, 0.8)
        vibration_total = calculate_vibration_total(vibration_x, vibration_y, vibration_z)

        rows.append({
            "temperature": round(temperature, 2),
            "vibration_total": round(vibration_total, 3),
            "rpm": 1450,
            "risk_level": "WARNING"
        })

    for _ in range(120):
        temperature = random.uniform(70, 90)
        vibration_x = random.uniform(1.0, 1.5)
        vibration_y = random.uniform(1.0, 1.5)
        vibration_z = random.uniform(1.0, 1.5)
        vibration_total = calculate_vibration_total(vibration_x, vibration_y, vibration_z)

        rows.append({
            "temperature": round(temperature, 2),
            "vibration_total": round(vibration_total, 3),
            "rpm": 1450,
            "risk_level": "CRITICAL"
        })

    df = pd.DataFrame(rows)
    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False)

    return df


def train_model():
    df = generate_training_data()

    X = df[["temperature", "vibration_total", "rpm"]]
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

    print("Model training completed")
    print("Accuracy:", accuracy)
    print(classification_report(y_test, predictions))

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_model()