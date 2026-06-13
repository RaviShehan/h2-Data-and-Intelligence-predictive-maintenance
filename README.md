# H2 Data Intelligence - Predictive Maintenance System

This project is the Data and Intelligence component of the Group H Predictive Maintenance System.

## Current Features

- Accept machine sensor data
- Extract vibration features
- Calculate total vibration
- Predict machine health status
- Return NORMAL, WARNING, or CRITICAL risk level
- Provide FastAPI API endpoint for dashboard integration

## API Endpoint

POST /predict

## Input Fields

- machine_id
- temperature
- vibration_x
- vibration_y
- vibration_z
- rpm

## Risk Levels

- NORMAL
- WARNING
- CRITICAL

## Tech Stack

- Python
- FastAPI
- Pydantic
- NumPy
- Uvicorn

## How to Run

```bash
venv\Scripts\python.exe -m uvicorn api.main:app --reload