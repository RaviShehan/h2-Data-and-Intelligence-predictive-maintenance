# H2 Data Intelligence Troubleshooting Guide

This document lists common errors that can happen while running the H2 Data and Intelligence component and how to fix them.

## 1. FastAPI server does not start

### Problem

```text
ModuleNotFoundError
```

### Fix

Run FastAPI from the project root folder:

```bash
venv\Scripts\python.exe -m uvicorn api.main:app --reload
```

Make sure the terminal path is the project root:

```text
C:\Users\ASUS\Desktop\h2-data-intelligence
```

## 2. PostgreSQL password error

### Problem

```text
DB_PASSWORD is missing
```

### Fix

Create a `.env` file in the project root.

Use `.env.example` as the template:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=h2_predictive_maintenance
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
```

Replace `your_postgresql_password` with the local PostgreSQL password.

Do not push `.env` to GitHub.

## 3. Database connection error

### Problem

FastAPI cannot connect to PostgreSQL.

### Fix

Check that PostgreSQL is running.

Check that this database exists:

```text
h2_predictive_maintenance
```

Check that `.env` contains the correct database username and password.

## 4. Kafka does not start

### Problem

Kafka container is not running.

### Fix

Start Kafka using Docker:

```bash
docker compose up -d
```

Check container status:

```bash
docker ps
```

Expected container name:

```text
h2-kafka
```

## 5. Kafka port already in use

### Problem

Docker says port `9092` is already in use.

### Fix

Stop old containers:

```bash
docker compose down
```

Then start again:

```bash
docker compose up -d
```

## 6. Raw NASA IMS dataset missing

### Problem

Real dataset preprocessing fails because raw files are missing.

### Fix

Make sure the raw NASA IMS dataset is extracted inside:

```text
data/raw/
```

Then run:

```bash
venv\Scripts\python.exe -m models.prepare_real_ims_data
```

## 7. Real model file missing

### Problem

```text
Real trained model not found
```

### Fix

Train the real model:

```bash
venv\Scripts\python.exe models/train_real_model.py
```

This should generate:

```text
models/trained_model_real.pkl
models/model_metadata_real.json
```

## 8. Evaluation report missing

### Problem

```text
Evaluation report not found
```

### Fix

Run:

```bash
venv\Scripts\python.exe models/evaluate_real_model.py
```

This should generate:

```text
models/evaluation_report_real.json
```

## 9. Feature importance report missing

### Problem

```text
Feature importance report not found
```

### Fix

Run:

```bash
venv\Scripts\python.exe models/feature_importance_real.py
```

This should generate:

```text
models/feature_importance_real.json
```

## 10. Tests fail after editing code

### Fix

First check which test failed:

```bash
venv\Scripts\python.exe -m pytest tests
```

Then check the related file.

Common test areas:

* API endpoint error → check `api/main.py`
* Validation error → check `api/validation.py`
* Feature error → check `features/feature_extraction.py`
* Signal processing error → check `features/signal_processing.py`
* Model error → check files inside `models/`
* Database error → check `database/db.py`

## 11. Markdown pasted into Python file by mistake

### Problem

Python shows syntax error near:

````text
```python
````

or:

```text
```

````

### Fix

Open the Python file and remove Markdown code block lines.

Python files should not contain:

```text
```python
````

or:

```text
```

````

## 12. Git tries to add raw dataset

### Problem

Git shows files inside:

```text
data/raw/
````

### Fix

Make sure `.gitignore` contains:

```text
data/raw/
```

Then check Git status again:

```bash
git status
```

Do not push the raw NASA IMS dataset to GitHub.

## 13. Safe shutdown steps

Before shutting down the laptop:

```bash
git status
```

If there are changes:

```bash
git add .
git commit -m "Save latest project updates"
git push
```

Stop FastAPI with:

```text
Ctrl + C
```

Stop Kafka:

```bash
docker compose down
```

Then shut down the laptop.
