# H2 Data Intelligence - Predictive Maintenance System

This project is the Data and Intelligence component of the Group H Predictive Maintenance System.

The system receives machine sensor readings, extracts vibration and temperature features, predicts machine health risk, and stores prediction history in PostgreSQL.

## Current Features

* FastAPI prediction API
* NORMAL, WARNING, and CRITICAL machine health prediction
* Sensor data simulator
* Kafka producer for streaming sensor data
* Kafka consumer for receiving sensor data
* PostgreSQL prediction history storage
* `/predictions` API endpoint to view stored prediction records
* Unit tests for prediction logic

## System Flow

```text
Sensor Simulator
      ↓
Kafka Producer
      ↓
Kafka Topic: machine.sensor.raw
      ↓
Kafka Consumer
      ↓
FastAPI /predict Endpoint
      ↓
Feature Extraction + Prediction
      ↓
PostgreSQL Database
```

## Tech Stack

* Python
* FastAPI
* Apache Kafka
* Docker
* PostgreSQL
* pgAdmin
* Pydantic
* kafka-python
* psycopg2
* pytest

## API Endpoints

### Health Check

```http
GET /
```

### Predict Machine Risk

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

Example response:

```json
{
  "prediction_id": 1,
  "risk_level": "CRITICAL",
  "failure_probability": 0.9,
  "recommended_action": "Immediate maintenance required"
}
```

### View Prediction History

```http
GET /predictions
```

## Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=h2_predictive_maintenance
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
```

The `.env` file is ignored by Git and should not be uploaded to GitHub.

## How to Run

### 1. Start Kafka with Docker

```bash
docker compose up -d
```

Check Kafka container:

```bash
docker ps
```

### 2. Run FastAPI Server

```bash
venv\Scripts\python.exe -m uvicorn api.main:app --reload
```

Open API documentation:

```text
http://127.0.0.1:8000/docs
```

### 3. Run Kafka Producer

Open a second terminal:

```bash
venv\Scripts\python.exe producer/kafka_sensor_producer.py
```

### 4. Run Kafka Consumer

Open a third terminal:

```bash
venv\Scripts\python.exe consumer/kafka_prediction_consumer.py
```

## Run Tests

```bash
venv\Scripts\python.exe -m pytest
```

Expected result:

```text
3 passed
```

## Project Status

Completed:

* FastAPI prediction service
* Kafka producer and consumer
* PostgreSQL prediction storage
* Prediction history endpoint
* Unit tests

Future improvements:

* Train machine learning model using real predictive maintenance dataset
* Add MLflow model tracking
* Add advanced signal processing using SciPy
* Add dashboard integration for H3 team
* Add model performance evaluation
