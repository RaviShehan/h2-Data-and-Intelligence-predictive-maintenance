# H2 Data Intelligence Setup Guide

This guide explains how to set up and run the H2 Data and Intelligence component locally.

## 1. Clone the Repository

```bash
git clone https://github.com/RaviShehan/h2-Data-and-Intelligence-predictive-maintenance.git
```

Go into the project folder:

```bash
cd h2-Data-and-Intelligence-predictive-maintenance
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Create Environment File

Copy the example environment file:

```bash
copy .env.example .env
```

Open `.env` and replace:

```env
DB_PASSWORD=your_postgresql_password
```

with your local PostgreSQL password.

Do not upload `.env` to GitHub.

## 5. Prepare PostgreSQL Database

Create a PostgreSQL database named:

```text
h2_predictive_maintenance
```

The FastAPI application will create the required `predictions` table automatically when the server starts.

## 6. Start Kafka

Start Kafka using Docker:

```bash
docker compose up -d
```

Check whether Kafka is running:

```bash
docker ps
```

Expected container name:

```text
h2-kafka
```

## 7. Prepare Real NASA IMS Dataset

The raw NASA IMS dataset should be stored locally inside:

```text
data/raw/
```

This folder is ignored by Git because the raw dataset is large.

Prepare the processed dataset:

```bash
venv\Scripts\python.exe -m models.prepare_real_ims_data
```

This generates:

```text
data/training_data_real.csv
```

## 8. Train Real Machine Learning Model

```bash
venv\Scripts\python.exe models/train_real_model.py
```

This generates:

```text
models/trained_model_real.pkl
models/model_metadata_real.json
```

## 9. Evaluate Real Machine Learning Model

```bash
venv\Scripts\python.exe models/evaluate_real_model.py
```

This generates:

```text
models/evaluation_report_real.json
```

## 10. Generate Feature Importance Report

```bash
venv\Scripts\python.exe models/feature_importance_real.py
```

This generates:

```text
models/feature_importance_real.json
```

## 11. Run FastAPI Server

```bash
venv\Scripts\python.exe -m uvicorn api.main:app --reload
```

Open API documentation:

```text
http://127.0.0.1:8000/docs
```

## 12. Run Tests

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
26 passed
```

## 13. Run Kafka Producer

Open a second terminal:

```bash
venv\Scripts\python.exe producer/kafka_sensor_producer.py
```

## 14. Run Kafka Consumer

Open a third terminal:

```bash
venv\Scripts\python.exe consumer/kafka_prediction_consumer.py
```

## 15. Stop the System

Stop FastAPI, producer, and consumer using:

```text
Ctrl + C
```

Stop Kafka:

```bash
docker compose down
```
