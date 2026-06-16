# H2 Data Intelligence Project Summary

## Project Name

H2 Data Intelligence - Predictive Maintenance System

## Project Purpose

The H2 component is responsible for converting raw machine sensor readings into predictive maintenance insights.

It receives sensor data, extracts vibration and signal-processing features, predicts machine health risk, detects anomalies, and stores prediction history.

## Main Problem Solved

Industrial machines can fail due to abnormal vibration, temperature, or operating conditions.

This system helps identify possible machine health issues early so maintenance can be planned before serious failure occurs.

## Main System Flow

```text
Sensor Simulator
      ↓
Kafka Producer
      ↓
Kafka Topic
      ↓
Kafka Consumer
      ↓
FastAPI Prediction API
      ↓
Feature Extraction
      ↓
SciPy Signal Processing
      ↓
RandomForestClassifier Model
      ↓
Anomaly Detection
      ↓
PostgreSQL Storage
```

## Main Technologies Used

* Python
* FastAPI
* Apache Kafka
* Docker
* PostgreSQL
* scikit-learn
* pandas
* NumPy
* SciPy
* pytest
* GitHub Actions

## Dataset Used

The project uses the NASA IMS Bearing Dataset.

The raw dataset is stored locally in:

```text
data/raw/
```

The processed dataset used for training is:

```text
data/training_data_real.csv
```

## Machine Learning Model

The system uses a RandomForestClassifier trained using NASA IMS vibration data.

The model predicts one of three machine health states:

* NORMAL
* WARNING
* CRITICAL

Current model accuracy:

```text
0.9645
```

## Feature Extraction

Basic vibration features:

* vibration_total
* vibration_rms
* vibration_mean
* vibration_peak
* vibration_std

SciPy signal-processing features:

* signal_rms
* signal_mean
* signal_peak
* signal_std
* signal_skewness
* signal_kurtosis
* spectral_energy

## API Endpoints

Main FastAPI endpoints:

* `GET /`
* `POST /predict`
* `GET /predictions`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`

## Anomaly Detection

The system detects abnormal sensor behavior such as:

* very high temperature
* abnormal vibration level
* very low rpm
* very high rpm

## Prediction Storage

Prediction results are stored in PostgreSQL.

Stored values include:

* machine ID
* raw sensor data
* extracted features
* risk level
* failure probability
* recommended action
* anomaly result
* timestamp

## Testing

The project includes automated pytest tests for:

* API endpoints
* feature extraction
* SciPy signal processing
* anomaly detection
* real NASA IMS model integration
* dataset structure
* feature importance report

Current expected test result:

```text
26 passed
```

## CI/CD

GitHub Actions is used to automatically run tests when code is pushed to GitHub.

Workflow file:

```text
.github/workflows/tests.yml
```

## Strong Viva Explanation

This project is not only a simple prediction API. It includes real-time streaming simulation using Kafka, REST API prediction using FastAPI, real NASA IMS dataset based machine learning, SciPy-based vibration signal processing, anomaly detection, PostgreSQL storage, feature importance explainability, automated tests, and GitHub Actions CI testing.
