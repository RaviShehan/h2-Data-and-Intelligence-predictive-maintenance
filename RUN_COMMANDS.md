# H2 Data Intelligence Run Commands

This document contains the most important commands for running, testing, and managing the H2 Data Intelligence component.

## 1. Open Project Folder

Project location:

```text
C:\Users\ASUS\Desktop\h2-data-intelligence
```

Make sure the terminal is opened in the project root.

## 2. Activate Virtual Environment

```bash
venv\Scripts\activate
```

Alternative command without activating:

```bash
venv\Scripts\python.exe
```

## 3. Run Tests

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
26 passed
```

## 4. Start FastAPI Server

```bash
venv\Scripts\python.exe -m uvicorn api.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 5. Start Kafka

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

Expected container:

```text
h2-kafka
```

## 6. Stop Kafka

```bash
docker compose down
```

## 7. Run Kafka Producer

Open a second terminal:

```bash
venv\Scripts\python.exe producer/kafka_sensor_producer.py
```

## 8. Run Kafka Consumer

Open a third terminal:

```bash
venv\Scripts\python.exe consumer/kafka_prediction_consumer.py
```

## 9. Prepare Real NASA IMS Dataset

```bash
venv\Scripts\python.exe -m models.prepare_real_ims_data
```

This generates:

```text
data/training_data_real.csv
```

## 10. Train Real Model

```bash
venv\Scripts\python.exe models/train_real_model.py
```

This generates:

```text
models/trained_model_real.pkl
models/model_metadata_real.json
```

## 11. Evaluate Real Model

```bash
venv\Scripts\python.exe models/evaluate_real_model.py
```

This generates:

```text
models/evaluation_report_real.json
```

## 12. Generate Feature Importance

```bash
venv\Scripts\python.exe models/feature_importance_real.py
```

This generates:

```text
models/feature_importance_real.json
```

## 13. Test Real Model Prediction Manually

```bash
venv\Scripts\python.exe -m models.test_real_model_prediction
```

## 14. Git Status

```bash
git status
```

Good output:

```text
nothing to commit, working tree clean
```

## 15. Save and Push Changes

```bash
git add .
git commit -m "Save latest project updates"
git push
```

## 16. Safe Shutdown Commands

Stop FastAPI, producer, or consumer:

```text
Ctrl + C
```

Stop Kafka:

```bash
docker compose down
```

Check Git:

```bash
git status
```

If there are changes:

```bash
git add .
git commit -m "Save latest project updates"
git push
```

## 17. Full Demo Command Order

Use this order during viva/demo:

```bash
venv\Scripts\python.exe -m pytest tests
docker compose up -d
venv\Scripts\python.exe -m uvicorn api.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

For full Kafka demo, open two more terminals:

```bash
venv\Scripts\python.exe producer/kafka_sensor_producer.py
```

```bash
venv\Scripts\python.exe consumer/kafka_prediction_consumer.py
```
