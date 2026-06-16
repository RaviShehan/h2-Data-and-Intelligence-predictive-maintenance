# H2 Data Intelligence API Reference

This document explains the FastAPI endpoints provided by the H2 Data and Intelligence component.

Base URL when running locally:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## 1. Health Check

### Endpoint

```http
GET /
```

### Purpose

Checks whether the FastAPI server is running.

### Example Response

```json
{
  "message": "H2 Predictive Maintenance API is running"
}
```

## 2. Predict Machine Risk

### Endpoint

```http
POST /predict
```

### Purpose

Receives machine sensor readings, extracts features, predicts machine health risk, performs anomaly detection, and stores the prediction result in PostgreSQL.

### Request Body

```json
{
  "machine_id": "MACHINE_01",
  "temperature": 75,
  "vibration_x": 1.2,
  "vibration_y": 1.0,
  "vibration_z": 1.1,
  "rpm": 1450
}
```

### Request Fields

| Field       | Type    | Description                    |
| ----------- | ------- | ------------------------------ |
| machine_id  | string  | Unique machine identifier      |
| temperature | float   | Machine temperature reading    |
| vibration_x | float   | Vibration value in X direction |
| vibration_y | float   | Vibration value in Y direction |
| vibration_z | float   | Vibration value in Z direction |
| rpm         | integer | Machine rotation speed         |

### Example Response

```json
{
  "prediction_id": 1,
  "input": {
    "machine_id": "MACHINE_01",
    "temperature": 75,
    "vibration_x": 1.2,
    "vibration_y": 1.0,
    "vibration_z": 1.1,
    "rpm": 1450
  },
  "features": {
    "machine_id": "MACHINE_01",
    "temperature": 75,
    "temperature_status": "HIGH",
    "vibration_total": 1.91,
    "vibration_rms": 1.103,
    "vibration_mean": 1.1,
    "vibration_peak": 1.2,
    "vibration_std": 0.082,
    "rpm": 1450,
    "signal_rms": 1.103025,
    "signal_mean": 1.1,
    "signal_peak": 1.2,
    "signal_std": 0.08165,
    "signal_skewness": 0.0,
    "signal_kurtosis": -1.5,
    "spectral_energy": 10.95
  },
  "prediction": {
    "machine_id": "MACHINE_01",
    "risk_level": "CRITICAL",
    "failure_probability": 0.46,
    "recommended_action": "Immediate maintenance required",
    "model_type": "RandomForestClassifier",
    "dataset_source": "NASA IMS Bearing Dataset",
    "probabilities": {
      "CRITICAL": 0.46,
      "NORMAL": 0.21,
      "WARNING": 0.33
    }
  },
  "anomaly_detection": {
    "is_anomaly": false,
    "anomaly_reasons": []
  }
}
```

## 3. View Prediction History

### Endpoint

```http
GET /predictions
```

### Purpose

Returns recently stored prediction records from PostgreSQL.

### Example Response

```json
[
  {
    "id": 1,
    "machine_id": "MACHINE_01",
    "temperature": 75,
    "vibration_total": 1.91,
    "rpm": 1450,
    "risk_level": "CRITICAL",
    "failure_probability": 0.46,
    "recommended_action": "Immediate maintenance required",
    "is_anomaly": false,
    "anomaly_reasons": [],
    "created_at": "2026-06-16T10:30:00"
  }
]
```

## 4. Model Information

### Endpoint

```http
GET /model-info
```

### Purpose

Returns lifecycle metadata about the active real-data trained machine learning model.

### Example Response

```json
{
  "model_name": "NASA IMS Bearing Risk Prediction Model",
  "model_type": "RandomForestClassifier",
  "model_file": "models/trained_model_real.pkl",
  "training_data": "data/training_data_real.csv",
  "dataset_source": "NASA IMS Bearing Dataset",
  "input_features": [
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
  ],
  "risk_classes": [
    "NORMAL",
    "WARNING",
    "CRITICAL"
  ],
  "accuracy": 0.9645,
  "model_available": true
}
```

## 5. Model Evaluation

### Endpoint

```http
GET /model-evaluation
```

### Purpose

Returns the saved evaluation report for the real NASA IMS trained RandomForestClassifier model.

### Response Includes

* Model type
* Dataset source
* Accuracy score
* Classification report
* Confusion matrix

### Example Response

```json
{
  "model_type": "RandomForestClassifier",
  "dataset_source": "NASA IMS Bearing Dataset",
  "dataset": "data/training_data_real.csv",
  "model_file": "models/trained_model_real.pkl",
  "accuracy": 0.9645,
  "classification_report": {},
  "confusion_matrix": []
}
```

## 6. Feature Importance

### Endpoint

```http
GET /feature-importance
```

### Purpose

Returns the feature importance report for the real NASA IMS RandomForestClassifier model.

This explains which vibration and SciPy signal-processing features are most important for machine health prediction.

### Example Response

```json
{
  "model_type": "RandomForestClassifier",
  "dataset_source": "NASA IMS Bearing Dataset",
  "feature_importance": [
    {
      "feature": "spectral_energy",
      "importance": 0.25
    }
  ]
}
```

## API Validation Rules

The API validates sensor readings before prediction.

| Field       | Rule                        |
| ----------- | --------------------------- |
| machine_id  | Cannot be empty             |
| temperature | Must be between 0 and 120   |
| vibration_x | Must be between 0 and 5     |
| vibration_y | Must be between 0 and 5     |
| vibration_z | Must be between 0 and 5     |
| rpm         | Must be between 0 and 10000 |

## Main API Files

| File                             | Purpose                          |
| -------------------------------- | -------------------------------- |
| `api/main.py`                    | FastAPI endpoints                |
| `api/validation.py`              | Input validation                 |
| `api/anomaly.py`                 | Anomaly detection                |
| `features/feature_extraction.py` | Feature extraction               |
| `features/signal_processing.py`  | SciPy signal processing          |
| `models/predict_real_model.py`   | Real model prediction            |
| `database/db.py`                 | PostgreSQL storage and retrieval |
