# H2 Data Intelligence - Predictive Maintenance System

This project is the Data and Intelligence component of the Group H Predictive Maintenance System.

The system receives machine sensor readings, extracts vibration and temperature features, predicts machine health risk, performs anomaly detection, and stores prediction history in PostgreSQL.

## Current Features

* FastAPI prediction API
* NORMAL, WARNING, and CRITICAL machine health prediction
* Sensor data simulator
* Kafka producer for streaming sensor data
* Kafka consumer for receiving sensor data
* PostgreSQL prediction history storage
* `/predictions` API endpoint to view stored prediction records
* Feature extraction from vibration and temperature sensor data
* SciPy-based signal feature extraction
* RandomForestClassifier ML model for machine risk prediction
* Real NASA IMS Bearing Dataset based model training
* Prediction probability output for each risk class
* Model lifecycle metadata
* `/model-info` endpoint for ML model lifecycle information
* `/model-evaluation` endpoint to view saved ML evaluation results
* Feature importance report for real NASA IMS model
* `/feature-importance` endpoint to view model feature importance
* Streaming anomaly detection for abnormal sensor behavior
* API tests verifying real NASA IMS model integration
* Tests verifying real NASA IMS processed dataset structure
* Unit tests for prediction logic, API endpoints, ML model, feature extraction, signal processing, and anomaly detection

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
Feature Extraction
      ↓
SciPy Signal Features
      ↓
Real-Data ML Prediction + Anomaly Detection
      ↓
PostgreSQL Database
```

## Real Dataset

The project uses the NASA IMS Bearing Dataset as the real predictive maintenance dataset.

The raw dataset is stored locally inside:

```text
data/raw/
```

This folder is ignored by Git because the raw dataset is large and should not be uploaded to GitHub.

The raw IMS vibration files are processed into a smaller CSV file:

```text
data/training_data_real.csv
```

The real-data preprocessing script is:

```text
models/prepare_real_ims_data.py
```

This script reads vibration files from the IMS dataset, extracts vibration and signal-processing features, assigns machine health labels, and creates the real training dataset.

## Dataset Documentation

A separate dataset documentation file is included to explain how the NASA IMS Bearing Dataset is used in this project.

Dataset documentation file:

```text
DATASET.md
```

The dataset documentation explains:

* Dataset source
* Raw dataset location
* Processed training dataset
* Preprocessing script
* Extracted vibration features
* Labeling method
* Model training and evaluation files
* Why raw data is not uploaded to GitHub

## Feature Extraction

The system extracts useful features from raw machine sensor readings before sending data to the machine learning model.

Raw input values from the API:

* temperature
* vibration_x
* vibration_y
* vibration_z
* rpm

Extracted features include:

* vibration_total
* vibration_rms
* vibration_mean
* vibration_peak
* vibration_std
* temperature_status

Feature extraction logic is implemented in:

```text
features/feature_extraction.py
```

Feature extraction is tested using:

```text
tests/test_feature_extraction.py
```

These features help the RandomForestClassifier classify the machine health state more accurately.

## SciPy Signal Processing

The project includes a SciPy-based signal processing module for extracting statistical and frequency-domain features from vibration signals.

Signal processing logic is implemented in:

```text
features/signal_processing.py
```

The extracted signal features include:

* signal_rms
* signal_mean
* signal_peak
* signal_std
* signal_skewness
* signal_kurtosis
* spectral_energy

The module uses:

* NumPy for numerical calculations
* SciPy for skewness and kurtosis calculations
* FFT-based spectral energy for frequency-domain analysis

Signal processing tests are implemented in:

```text
tests/test_signal_processing.py
```

This supports the H2 requirement of feature extraction from vibration signals using SciPy.

## Machine Learning Model

The prediction service uses a trained machine learning model to classify machine health risk.

### Active Model Used

* RandomForestClassifier
* Trained using real NASA IMS Bearing Dataset vibration data
* Enhanced using SciPy-based statistical and frequency-domain signal features
* Input features:

  * vibration_total
  * vibration_rms
  * vibration_mean
  * vibration_peak
  * vibration_std
  * signal_rms
  * signal_mean
  * signal_peak
  * signal_std
  * signal_skewness
  * signal_kurtosis
  * spectral_energy

### Real Model Files

* `data/training_data_real.csv` - processed NASA IMS training dataset
* `models/prepare_real_ims_data.py` - converts raw IMS vibration files into a training CSV
* `models/train_real_model.py` - trains the real-data machine learning model
* `models/predict_real_model.py` - loads the real-data model and performs prediction
* `models/trained_model_real.pkl` - saved RandomForestClassifier model trained using NASA IMS data
* `models/model_metadata_real.json` - metadata for the real-data model
* `models/test_real_model_prediction.py` - simple script to test real model prediction

### Real Model Performance

The real-data model was trained using vibration and SciPy signal-processing features extracted from the NASA IMS Bearing Dataset.

Current real model accuracy:

```text
0.9645
```

After adding SciPy-based statistical and frequency-domain signal features, the real NASA IMS model accuracy improved to 0.9645.

This means the system now uses a real predictive maintenance dataset instead of only generated sample data.

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
  "failure_probability": 0.46,
  "recommended_action": "Immediate maintenance required",
  "model_type": "RandomForestClassifier",
  "dataset_source": "NASA IMS Bearing Dataset",
  "probabilities": {
    "CRITICAL": 0.46,
    "NORMAL": 0.21,
    "WARNING": 0.33
  }
}
```

## Model Card

A model card is included to document the real NASA IMS Bearing prediction model.

Model card file:

```text
MODEL_CARD.md
```

The model card explains:

* Dataset used
* Model type
* Input features
* Output classes
* Model performance
* API integration
* Current limitations
* Future improvements

This helps make the machine learning part more transparent and report-ready.

## Model Lifecycle Metadata

The system stores model lifecycle information in metadata files after model training.

Real model metadata file:

```text
models/model_metadata_real.json
```

The metadata file includes:

* Model name
* Model type
* Model file path
* Training dataset path
* Training timestamp
* Dataset source
* Input features
* Risk classes
* Accuracy score

This helps track which model version is currently used by the prediction API.

## Model Evaluation

The real-data RandomForestClassifier model can be evaluated using the processed NASA IMS Bearing Dataset.

Evaluation script:

```text
models/evaluate_real_model.py
```

Run real model evaluation:

```bash
venv\Scripts\python.exe models/evaluate_real_model.py
```

The evaluation output includes:

* Accuracy score
* Classification report
* Confusion matrix

The real evaluation result is saved to:

```text
models/evaluation_report_real.json
```

Current real model accuracy:

```text
0.9645
```

This verifies how well the model predicts the three machine health classes:

* NORMAL
* WARNING
* CRITICAL

## Feature Importance

The project generates a feature importance report for the real NASA IMS RandomForestClassifier model.

Feature importance script:

```text
models/feature_importance_real.py
```

Run feature importance generation:

```bash
venv\Scripts\python.exe models/feature_importance_real.py
```

The feature importance report is saved to:

```text
models/feature_importance_real.json
```

This helps explain which vibration and SciPy signal-processing features contribute most to the machine health prediction.

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
* SciPy
* joblib
* httpx

## API Endpoints

### Health Check

```http
GET /
```

This endpoint checks whether the API server is running.

### Model Information

```http
GET /model-info
```

This endpoint returns machine learning model lifecycle information.

Example response:

```json
{
  "model_name": "NASA IMS Bearing Risk Prediction Model",
  "model_type": "RandomForestClassifier",
  "model_file": "models/trained_model_real.pkl",
  "training_data": "data/training_data_real.csv",
  "dataset_source": "NASA IMS Bearing Dataset",
  "trained_at": "2026-06-15T14:00:00",
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

### Model Evaluation

```http
GET /model-evaluation
```

This endpoint returns the saved real machine learning model evaluation report.

The response includes:

* Model type
* Dataset source
* Accuracy score
* Classification report
* Confusion matrix

Example response:

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

### Feature Importance

```http
GET /feature-importance
```

This endpoint returns the feature importance report for the real NASA IMS RandomForestClassifier model.

The response includes:

* Model type
* Dataset source
* Feature importance values

Example response:

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

### Predict Machine Risk

```http
POST /predict
```

This endpoint receives machine sensor readings, extracts features, predicts machine health risk using the real-data trained model, performs anomaly detection, and stores the prediction result in PostgreSQL.

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

### View Prediction History

```http
GET /predictions
```

This endpoint returns recently stored prediction records from PostgreSQL.

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

### 5. Prepare Real NASA IMS Dataset

The raw NASA IMS files should be extracted locally inside:

```text
data/raw/
```

Then run:

```bash
venv\Scripts\python.exe -m models.prepare_real_ims_data
```

This generates:

```text
data/training_data_real.csv
```

### 6. Train Real ML Model

```bash
venv\Scripts\python.exe models/train_real_model.py
```

This generates:

* `models/trained_model_real.pkl`
* `models/model_metadata_real.json`

### 7. Test Real Model Prediction

```bash
venv\Scripts\python.exe -m models.test_real_model_prediction
```

### 8. Evaluate Real ML Model

```bash
venv\Scripts\python.exe models/evaluate_real_model.py
```

This generates:

```text
models/evaluation_report_real.json
```

### 9. Generate Feature Importance Report

```bash
venv\Scripts\python.exe models/feature_importance_real.py
```

This generates:

```text
models/feature_importance_real.json
```

## Run Tests

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
22 passed
```

## Project Status

Completed:

* FastAPI prediction service
* Kafka producer and consumer
* PostgreSQL prediction storage
* Prediction history endpoint
* Feature extraction module
* SciPy signal processing module
* RandomForestClassifier model training
* NASA IMS real dataset preprocessing
* Real-data RandomForestClassifier training
* SciPy-enhanced real-data model training
* FastAPI connected to real-data trained model
* Prediction probability output
* Model lifecycle metadata generation
* `/model-info` endpoint for model lifecycle information
* Real model evaluation report generation
* `/model-evaluation` endpoint
* Feature importance report generation
* `/feature-importance` endpoint
* API test for feature importance endpoint
* Streaming anomaly detection module
* Model card for NASA IMS prediction model
* Dataset documentation for NASA IMS Bearing Dataset
* Unit tests for prediction logic
* Unit tests for ML model
* Unit tests for API endpoints
* Unit tests for anomaly detection
* Unit tests for feature extraction
* Unit tests for signal processing features
* Unit tests for real NASA IMS processed dataset
* Unit test for real NASA IMS trained model
* API test proving `/predict` uses NASA IMS trained model

Future improvements:

* Add MLflow model tracking
* Add dashboard integration for H3 team
* Add deployment support for production environment
* Train using all IMS test sets instead of only `2nd_test`
