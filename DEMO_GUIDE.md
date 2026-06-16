# H2 Data Intelligence Demo Guide

This document explains how to demonstrate the H2 Data and Intelligence component during viva or project presentation.

## 1. Open Project

Open the project folder in VS Code:

```text
C:\Users\ASUS\Desktop\h2-data-intelligence
```

Open a terminal in VS Code.

## 2. Check Project Status

```bash
git status
```

Expected output:

```text
nothing to commit, working tree clean
```

## 3. Run Tests First

Run all tests to prove the system works:

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
26 passed
```

This shows that API endpoints, feature extraction, signal processing, anomaly detection, real NASA IMS model integration, and feature importance tests are working.

## 4. Start Kafka Using Docker

```bash
docker compose up -d
```

Check whether Kafka is running:

```bash
docker ps
```

Expected container:

```text
h2-kafka
```

Kafka is used to simulate real-time machine sensor data streaming.

## 5. Start FastAPI Server

```bash
venv\Scripts\python.exe -m uvicorn api.main:app --reload
```

Open API documentation in browser:

```text
http://127.0.0.1:8000/docs
```

## 6. Test Health Check Endpoint

Endpoint:

```http
GET /
```

Expected result:

```json
{
  "message": "H2 Predictive Maintenance API is running"
}
```

This proves that the FastAPI server is running.

## 7. Test Model Information Endpoint

Endpoint:

```http
GET /model-info
```

This shows:

* model name
* model type
* dataset source
* input features
* accuracy
* model file availability

Use this endpoint to explain the model lifecycle metadata.

## 8. Test Model Evaluation Endpoint

Endpoint:

```http
GET /model-evaluation
```

This shows:

* model type
* dataset source
* accuracy
* classification report
* confusion matrix

Use this endpoint to explain how the real NASA IMS model was evaluated.

## 9. Test Feature Importance Endpoint

Endpoint:

```http
GET /feature-importance
```

This shows which vibration and SciPy signal-processing features are most important for prediction.

Use this endpoint to explain model explainability.

## 10. Test Prediction Endpoint

Endpoint:

```http
POST /predict
```

Example request:

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

Expected response includes:

* input sensor data
* extracted features
* SciPy signal features
* predicted risk level
* failure probability
* recommended action
* anomaly detection result
* prediction ID saved in PostgreSQL

## 11. Test Prediction History Endpoint

Endpoint:

```http
GET /predictions
```

This shows prediction records stored in PostgreSQL.

Use this endpoint to explain that prediction history is saved for later monitoring and reporting.

## 12. Run Kafka Producer

Open a second terminal:

```bash
venv\Scripts\python.exe producer/kafka_sensor_producer.py
```

This sends simulated sensor readings to Kafka.

## 13. Run Kafka Consumer

Open a third terminal:

```bash
venv\Scripts\python.exe consumer/kafka_prediction_consumer.py
```

This receives Kafka sensor messages and sends them to the FastAPI prediction endpoint.

This demonstrates the full streaming pipeline.

## 14. Full Demo Flow to Explain

```text
Sensor Simulator
      ↓
Kafka Producer
      ↓
Kafka Topic
      ↓
Kafka Consumer
      ↓
FastAPI /predict
      ↓
Feature Extraction
      ↓
SciPy Signal Processing
      ↓
NASA IMS RandomForestClassifier
      ↓
Anomaly Detection
      ↓
PostgreSQL Storage
```

## 15. Strong Demo Explanation

The H2 component receives machine sensor readings, processes them using feature extraction and SciPy signal processing, predicts machine health risk using a real NASA IMS trained RandomForestClassifier model, detects abnormal values, stores results in PostgreSQL, and exposes all results through FastAPI endpoints.

## 16. Stop the Demo

Stop FastAPI, producer, and consumer by pressing:

```text
Ctrl + C
```

Stop Kafka:

```bash
docker compose down
```
