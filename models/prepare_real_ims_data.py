import os
import math

import numpy as np
import pandas as pd


RAW_DATA_DIR = "data/raw/IMS/extracted/2nd_test/2nd_test"
OUTPUT_PATH = "data/training_data_real.csv"


def read_vibration_file(file_path):
    data = pd.read_csv(file_path, sep=r"\s+", header=None)

    values = data.values.flatten()
    values = values.astype(float)

    return values


def extract_real_features(values):
    vibration_rms = math.sqrt(np.mean(values ** 2))
    vibration_mean = np.mean(values)
    vibration_peak = np.max(np.abs(values))
    vibration_std = np.std(values)

    return {
        "vibration_total": round(float(vibration_rms), 6),
        "vibration_rms": round(float(vibration_rms), 6),
        "vibration_mean": round(float(vibration_mean), 6),
        "vibration_peak": round(float(vibration_peak), 6),
        "vibration_std": round(float(vibration_std), 6)
    }


def assign_risk_level(index, total_files):
    progress = index / total_files

    if progress < 0.60:
        return "NORMAL"
    elif progress < 0.85:
        return "WARNING"
    else:
        return "CRITICAL"


def prepare_real_dataset():
    files = sorted(os.listdir(RAW_DATA_DIR))

    rows = []

    for index, filename in enumerate(files):
        file_path = os.path.join(RAW_DATA_DIR, filename)

        if not os.path.isfile(file_path):
            continue

        values = read_vibration_file(file_path)
        features = extract_real_features(values)

        risk_level = assign_risk_level(index, len(files))

        row = {
            "source_file": filename,
            "temperature": 0,
            "rpm": 0,
            **features,
            "risk_level": risk_level
        }

        rows.append(row)

    df = pd.DataFrame(rows)

    os.makedirs("data", exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("Real IMS dataset prepared")
    print(f"Total rows: {len(df)}")
    print(f"Saved to: {OUTPUT_PATH}")
    print()
    print(df["risk_level"].value_counts())


if __name__ == "__main__":
    prepare_real_dataset()

