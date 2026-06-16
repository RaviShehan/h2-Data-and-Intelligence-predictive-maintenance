# H2 Data Intelligence Database Schema

This document explains the PostgreSQL database structure used by the H2 Data and Intelligence component.

## Database Name

```text
h2_predictive_maintenance
```

## Main Table

The main table used by the system is:

```text
predictions
```

This table stores machine prediction history.

## Purpose of the `predictions` Table

The `predictions` table stores each prediction made by the FastAPI `/predict` endpoint.

It stores:

* machine ID
* raw sensor values
* extracted features
* predicted risk level
* failure probability
* recommended action
* anomaly detection result
* timestamp

## Table Structure

| Column              | Type               | Purpose                                 |
| ------------------- | ------------------ | --------------------------------------- |
| id                  | SERIAL PRIMARY KEY | Unique prediction record ID             |
| machine_id          | VARCHAR(50)        | Machine identifier                      |
| temperature         | DOUBLE PRECISION   | Machine temperature reading             |
| vibration_total     | DOUBLE PRECISION   | Total vibration magnitude               |
| rpm                 | INTEGER            | Machine rotation speed                  |
| risk_level          | VARCHAR(20)        | Predicted risk level                    |
| failure_probability | DOUBLE PRECISION   | Probability of predicted risk           |
| recommended_action  | TEXT               | Suggested maintenance action            |
| sensor_data         | JSONB              | Original input sensor data              |
| features            | JSONB              | Extracted vibration and signal features |
| is_anomaly          | BOOLEAN            | Whether anomaly was detected            |
| anomaly_reasons     | JSONB              | Reasons for anomaly detection           |
| created_at          | TIMESTAMP          | Time when prediction was stored         |

## Stored Risk Levels

The model predicts one of the following risk levels:

* NORMAL
* WARNING
* CRITICAL

## Example Stored Prediction

```json
{
  "machine_id": "MACHINE_01",
  "temperature": 75,
  "vibration_total": 1.91,
  "rpm": 1450,
  "risk_level": "CRITICAL",
  "failure_probability": 0.46,
  "recommended_action": "Immediate maintenance required",
  "is_anomaly": false,
  "anomaly_reasons": []
}
```

## JSONB Fields

### `sensor_data`

The `sensor_data` column stores the original input values.

Example:

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

### `features`

The `features` column stores extracted features.

Example:

```json
{
  "vibration_total": 1.91,
  "vibration_rms": 1.103,
  "vibration_mean": 1.1,
  "vibration_peak": 1.2,
  "vibration_std": 0.082,
  "signal_rms": 1.103025,
  "signal_mean": 1.1,
  "signal_peak": 1.2,
  "signal_std": 0.08165,
  "signal_skewness": 0.0,
  "signal_kurtosis": -1.5,
  "spectral_energy": 10.95
}
```

## Database Logic File

Database connection and query logic is implemented in:

```text
database/db.py
```

This file handles:

* PostgreSQL connection
* prediction table creation
* saving prediction results
* retrieving recent prediction records

## API Endpoints Using Database

The following endpoints interact with the database:

| Endpoint           | Purpose                             |
| ------------------ | ----------------------------------- |
| `POST /predict`    | Saves prediction result             |
| `GET /predictions` | Retrieves recent prediction history |

## Why PostgreSQL Is Used

PostgreSQL is used because it supports:

* structured relational data
* JSONB storage for flexible sensor and feature data
* reliable prediction history storage
* easy integration with FastAPI using psycopg2

## Viva Explanation

During viva, the database can be explained like this:

The H2 component stores every prediction result in PostgreSQL. The database stores raw sensor readings, extracted features, predicted risk level, failure probability, recommended maintenance action, anomaly result, and timestamp. JSONB fields are used to store flexible sensor data and extracted feature data.
