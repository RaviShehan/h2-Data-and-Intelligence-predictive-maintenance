# H2 Data Intelligence Final Checklist

This checklist should be used before viva, demo, or final submission.

## 1. GitHub Repository Check

Run:

```bash
git status
```

Expected:

```text
nothing to commit, working tree clean
```

Make sure the latest work is pushed to GitHub:

```bash
git push
```

## 2. Secret File Check

Make sure `.env` is not pushed to GitHub.

The project should contain:

```text
.env.example
```

The project should not upload:

```text
.env
```

## 3. Raw Dataset Check

Make sure the raw NASA IMS dataset is not pushed to GitHub.

The raw dataset folder should be ignored:

```text
data/raw/
```

The processed dataset can be used by the project:

```text
data/training_data_real.csv
```

## 4. Test Check

Run all tests:

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
26 passed
```

This proves that API endpoints, feature extraction, SciPy signal processing, anomaly detection, real NASA IMS model integration, and feature importance tests are working.

## 5. FastAPI Check

Start FastAPI:

```bash
venv\Scripts\python.exe -m uvicorn api.main:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Check these endpoints:

* `GET /`
* `POST /predict`
* `GET /predictions`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`

## 6. Model Files Check

Make sure these files exist:

```text
models/trained_model_real.pkl
models/model_metadata_real.json
models/evaluation_report_real.json
models/feature_importance_real.json
```

## 7. Dataset Files Check

Make sure these files exist:

```text
data/training_data_real.csv
DATASET.md
```

## 8. Documentation Check

Make sure these documentation files exist:

```text
README.md
SETUP.md
ARCHITECTURE.md
PROJECT_STRUCTURE.md
API_REFERENCE.md
MODEL_CARD.md
DATASET.md
DEMO_GUIDE.md
VIVA_NOTES.md
TROUBLESHOOTING.md
SECURITY.md
FINAL_CHECKLIST.md
```

## 9. Demo Check

For full streaming demo, start Kafka:

```bash
docker compose up -d
```

Check Kafka:

```bash
docker ps
```

Expected container:

```text
h2-kafka
```

Run producer in one terminal:

```bash
venv\Scripts\python.exe producer/kafka_sensor_producer.py
```

Run consumer in another terminal:

```bash
venv\Scripts\python.exe consumer/kafka_prediction_consumer.py
```

## 10. Strong Viva Points

Mention these points during viva:

* Real NASA IMS Bearing Dataset is used
* SciPy signal processing is used
* RandomForestClassifier predicts machine health risk
* Accuracy is 0.9645
* API provides model info, evaluation, and feature importance
* Anomaly detection is included
* PostgreSQL stores prediction history
* Kafka simulates real-time streaming
* Automated tests verify the system
* `.env` and raw dataset are safely ignored by Git

## 11. Shutdown After Demo

Stop FastAPI, producer, and consumer:

```text
Ctrl + C
```

Stop Kafka:

```bash
docker compose down
```

Check Git one final time:

```bash
git status
```
