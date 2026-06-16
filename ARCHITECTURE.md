# H2 Data Intelligence Architecture

This document explains the architecture of the H2 Data and Intelligence component of the Group H Predictive Maintenance System.

## Purpose of H2

H2 is responsible for receiving machine sensor data, extracting useful features, predicting machine health risk, detecting abnormal sensor behavior, and storing prediction results.

The main goal of H2 is to convert raw machine sensor readings into meaningful predictive maintenance insights.

## High-Level System Flow

```text
Sensor Simulator
      ↓
Kafka Producer
      ↓
Kafka Topic: machine.sensor.raw
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
PostgreSQL Database
```

## Main Components

### 1. Sensor Simulator

The sensor simulator generates sample machine sensor readings.

Example sensor values:

* temperature
* vibration_x
* vibration_y
* vibration_z
* rpm

These values represent the condition of a machine at a given time.

### 2. Kafka Producer

The Kafka producer sends sensor readings to a Kafka topic.

Kafka is used to simulate real-time streaming data from machines.

Kafka topic used:

```text
machine.sensor.raw
```

### 3. Kafka Consumer

The Kafka consumer listens to the Kafka topic and receives incoming machine sensor readings.

After receiving sensor data, the consumer sends the data to the FastAPI prediction endpoint.

### 4. FastAPI Prediction API

FastAPI provides REST API endpoints for prediction, model information, model evaluation, feature importance, and prediction history.

Main endpoints:

* `GET /`
* `POST /predict`
* `GET /predictions`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`

### 5. Feature Extraction

Raw vibration values are converted into useful machine learning features.

Extracted features include:

* vibration_total
* vibration_rms
* vibration_mean
* vibration_peak
* vibration_std
* temperature_status

Feature extraction file:

```text
features/feature_extraction.py
```

### 6. SciPy Signal Processing

The system uses SciPy and NumPy to extract additional statistical and frequency-domain signal features.

Signal features include:

* signal_rms
* signal_mean
* signal_peak
* signal_std
* signal_skewness
* signal_kurtosis
* spectral_energy

Signal processing file:

```text
features/signal_processing.py
```

These features improve the quality of machine health prediction.

### 7. Machine Learning Model

The system uses a RandomForestClassifier trained using the NASA IMS Bearing Dataset.

The model predicts one of three machine health states:

* NORMAL
* WARNING
* CRITICAL

Model files:

```text
models/trained_model_real.pkl
models/model_metadata_real.json
models/evaluation_report_real.json
models/feature_importance_real.json
```

### 8. Feature Importance

The system generates a feature importance report for the trained RandomForestClassifier model.

Feature importance file:

```text
models/feature_importance_real.json
```

Feature importance helps explain which vibration and SciPy signal-processing features contribute most to the final prediction.

This is useful for viva because it makes the machine learning model more explainable.

### 9. Anomaly Detection

In addition to ML prediction, the system checks for abnormal sensor behavior using threshold-based anomaly detection.

Anomalies can be detected for:

* very high temperature
* abnormal vibration level
* very low rpm
* very high rpm

Anomaly detection file:

```text
api/anomaly.py
```

### 10. PostgreSQL Database

Prediction results are stored in PostgreSQL.

Stored information includes:

* machine_id
* sensor data
* extracted features
* predicted risk level
* failure probability
* recommended action
* anomaly result
* created timestamp

Database logic file:

```text
database/db.py
```

## Why This Architecture Is Useful

This architecture supports predictive maintenance because it combines:

* real-time streaming using Kafka
* REST API prediction using FastAPI
* real dataset based machine learning
* SciPy-based vibration signal analysis
* model explainability using feature importance
* anomaly detection
* persistent storage using PostgreSQL
* automated tests for reliability

## H2 Responsibility in the Full Group Project

H2 focuses on the Data and Intelligence layer.

Other teams can use H2 outputs for:

* dashboard visualization
* alerts
* maintenance planning
* reporting
* machine health monitoring
