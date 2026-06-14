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
* RandomForestClassifier ML model for machine risk prediction
* Prediction probability output for each risk class
* `/model-info` endpoint for ML model lifecycle information
* Streaming anomaly detection for abnormal sensor behavior


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

## Machine Learning Model

The prediction service uses a trained machine learning model to classify machine health risk.

### Model Used

* RandomForestClassifier
* Trained using generated predictive maintenance training data
* Input features:

  * temperature
  * vibration_total
  * rpm

### Model Files

* `data/training_data.csv` - generated training dataset
* `models/train_model.py` - trains the machine learning model
* `models/predict_model.py` - loads the trained model and performs prediction
* `models/trained_model.pkl` - saved trained Random Forest model

### Model Output

The model predicts one of the following machine health states:

* NORMAL
* WARNING
* CRITICAL

The API response also includes prediction probabilities for each risk class.

Example model output:

```json
{
  "risk_level": "CRITICAL",
  "failure_probability": 1.0,
  "model_type": "RandomForestClassifier",
  "probabilities": {
    "CRITICAL": 1.0,
    "NORMAL": 0.0,
    "WARNING": 0.0
  }
}
```
## Model Evaluation

The trained RandomForestClassifier model can be evaluated using the saved training dataset.

Evaluation script:

```text
models/evaluate_model.py
```

Run model evaluation:

```bash
venv\Scripts\python.exe models/evaluate_model.py
```

The evaluation output includes:

* Accuracy score
* Classification report
* Confusion matrix

This helps verify how well the model predicts the three machine health classes:

* NORMAL
* WARNING
* CRITICAL


## Streaming Anomaly Detection

The system includes anomaly detection logic to identify abnormal machine sensor behavior during prediction.

The anomaly detection module checks extracted sensor features such as:

* temperature
* vibration_total
* rpm

An anomaly is detected when sensor values exceed predefined safety thresholds.

Examples of detected anomalies:

* Very high temperature detected
* Abnormal vibration level detected
* RPM too low for normal operation
* RPM too high for normal operation

Anomaly detection is integrated with the `/predict` API response.

Example output:

```json
{
  "anomaly_detection": {
    "is_anomaly": true,
    "anomaly_reasons": [
      "Very high temperature detected"
    ]
  }
}
```

This supports real-time monitoring of abnormal machine behavior in the predictive maintenance pipeline.



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
* scikit-learn
* pandas
* NumPy
* joblib

## API Endpoints

### Health Check

```http
GET /

Model Information
GET /model-info

This endpoint returns information about the trained machine learning model used by the prediction service.

Example response:

{
  "model_name": "Machine Health Risk Prediction Model",
  "model_type": "RandomForestClassifier",
  "model_file": "models/trained_model.pkl",
  "model_available": true,
  "input_features": [
    "temperature",
    "vibration_total",
    "rpm"
  ],
  "risk_classes": [
    "NORMAL",
    "WARNING",
    "CRITICAL"
  ]
}

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
* RandomForestClassifier model training
* ML model integration with FastAPI
* Streaming anomaly detection module
* Unit tests for anomaly detection

Future improvements:

* Train machine learning model using real predictive maintenance dataset
* Add MLflow model tracking
* Add advanced signal processing using SciPy
* Add dashboard integration for H3 team
* Add model performance evaluation
* Model information endpoint for ML lifecycle visibility
