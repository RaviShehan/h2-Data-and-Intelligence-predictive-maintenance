# Group H Predictive Maintenance System - Full H1 to H4 Overview

This document explains how the full Group H Predictive Maintenance System works from H1 to H4.

## Full System Components

The system is divided into four main parts:

| Component | Responsibility                                                                                    |
| --------- | ------------------------------------------------------------------------------------------------- |
| H1        | Edge device simulation and sensor telemetry generation                                            |
| H2        | Data intelligence, feature extraction, ML prediction, anomaly detection, and database storage     |
| H3        | Dashboard visualization for predictions, model information, feature importance, and system health |
| H4        | Platform monitoring, CI/CD, security practices, and system health checks                          |

## Full System Flow

```text
H1 Edge Device Simulator
      ↓
Kafka Topic: machine.sensor.raw
      ↓
H2 Kafka Consumer
      ↓
H2 FastAPI Prediction API
      ↓
Feature Extraction + SciPy Signal Processing
      ↓
NASA IMS RandomForestClassifier Model
      ↓
Anomaly Detection
      ↓
PostgreSQL Prediction Storage
      ↓
H3 Streamlit Dashboard
      ↓
H4 System Health Monitoring
```

## H1 - Edge Device Simulator

H1 simulates edge-level machine sensor data collection.

The edge simulator generates machine telemetry values such as:

* machine_id
* temperature
* vibration_x
* vibration_y
* vibration_z
* rpm
* timestamp

H1 also performs simple edge-side processing:

* sensor data generation
* basic filtering
* telemetry validation
* sending validated data to Kafka

Main H1 file:

```text
edge/edge_device_simulator.py
```

Kafka topic used:

```text
machine.sensor.raw
```

## H2 - Data Intelligence

H2 is the main data intelligence layer.

H2 receives machine sensor data, extracts useful features, predicts machine health risk, detects anomalies, and stores prediction results.

Main H2 responsibilities:

* receive sensor readings from API or Kafka consumer
* validate sensor input
* extract vibration features
* extract SciPy signal-processing features
* predict machine health using real NASA IMS trained RandomForestClassifier
* detect abnormal sensor behavior
* store prediction history in PostgreSQL
* expose prediction and model endpoints through FastAPI

Main H2 endpoints:

* `GET /`
* `POST /predict`
* `GET /predictions`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`
* `GET /system-health`

Main H2 technologies:

* FastAPI
* PostgreSQL
* Kafka consumer
* scikit-learn
* NumPy
* SciPy
* pandas

## H3 - Dashboard Visualization

H3 provides a Streamlit dashboard for visualizing H2 outputs.

The dashboard shows:

* latest prediction records
* machine risk summary
* anomaly status
* model information
* model evaluation report
* feature importance chart
* H4 system health status

Main H3 file:

```text
dashboard/app.py
```

Run dashboard:

```bash
venv\Scripts\python.exe -m streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

## H4 - Platform Monitoring and Security

H4 adds platform-level monitoring and project safety features.

Implemented H4 features include:

* `/system-health` endpoint
* database connection check
* model file availability check
* evaluation report availability check
* feature importance report availability check
* GitHub Actions automated testing
* `.env` security practice
* `.env.example` safe template
* raw dataset ignored using `.gitignore`
* security documentation
* CI/CD documentation

System health endpoint:

```http
GET /system-health
```

Example system health response:

```json
{
  "system": "H4 Platform Monitoring",
  "overall_status": "healthy",
  "api_status": "running",
  "database_status": "connected",
  "model_file_available": true,
  "evaluation_report_available": true,
  "feature_importance_available": true
}
```

## Full Demo Order

Use this order to run the full H1-H4 system.

### 1. Start Kafka

```bash
docker compose up -d
```

### 2. Start FastAPI

```bash
venv\Scripts\python.exe -m uvicorn api.main:app --reload
```

### 3. Start H2 Kafka Consumer

```bash
venv\Scripts\python.exe consumer/kafka_prediction_consumer.py
```

### 4. Start H1 Edge Simulator

```bash
venv\Scripts\python.exe edge\edge_device_simulator.py
```

### 5. Start H3 Dashboard

```bash
venv\Scripts\python.exe -m streamlit run dashboard/app.py
```

## How to Verify the Full System

Open FastAPI Swagger:

```text
http://127.0.0.1:8000/docs
```

Check:

* `GET /`
* `GET /predictions`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`
* `GET /system-health`

Open Streamlit dashboard:

```text
http://localhost:8501
```

Check dashboard tabs:

* Prediction History
* Risk Summary
* Model Information
* Feature Importance
* System Health

## Testing

Run all tests:

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
27 passed
```

## Strong Viva Explanation

The full system includes H1 edge telemetry generation, H2 data intelligence and machine learning prediction, H3 dashboard visualization, and H4 platform monitoring. H1 sends validated machine telemetry to Kafka. H2 consumes that data, extracts vibration and SciPy signal-processing features, predicts machine health using a NASA IMS trained RandomForestClassifier, detects anomalies, and stores results in PostgreSQL. H3 visualizes predictions, model information, feature importance, and system health. H4 adds monitoring, CI/CD, security practices, and system health checks.
