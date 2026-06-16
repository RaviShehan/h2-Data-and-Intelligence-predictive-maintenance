# H2 Data Intelligence Project Structure

This document explains the folder and file structure of the H2 Data and Intelligence component.

## Root Files

| File                 | Purpose                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------- |
| `README.md`          | Main project overview, features, API endpoints, setup summary, and project status       |
| `SETUP.md`           | Step-by-step guide to set up and run the project locally                                |
| `ARCHITECTURE.md`    | Explains the system architecture and component responsibilities                         |
| `VIVA_NOTES.md`      | Short answers for explaining the project during viva                                    |
| `DEMO_GUIDE.md`      | Step-by-step guide for demonstrating the project                                        |
| `DATASET.md`         | Documents how the NASA IMS Bearing Dataset is used                                      |
| `MODEL_CARD.md`      | Documents the machine learning model, performance, limitations, and future improvements |
| `.env.example`       | Safe example environment file without real passwords                                    |
| `.gitignore`         | Prevents virtual environment, raw dataset, cache files, and secrets from being pushed   |
| `docker-compose.yml` | Starts Kafka using Docker                                                               |
| `requirements.txt`   | Lists Python dependencies needed for the project                                        |

## `api/`

This folder contains the FastAPI application and API-related logic.

| File            | Purpose                                       |
| --------------- | --------------------------------------------- |
| `main.py`       | Main FastAPI app with API endpoints           |
| `validation.py` | Pydantic input validation for sensor readings |
| `anomaly.py`    | Threshold-based anomaly detection logic       |
| `prediction.py` | Basic prediction-related logic                |

Main API endpoints include:

* `GET /`
* `POST /predict`
* `GET /predictions`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`

## `features/`

This folder contains feature extraction and signal processing logic.

| File                    | Purpose                                                                  |
| ----------------------- | ------------------------------------------------------------------------ |
| `feature_extraction.py` | Extracts vibration and temperature features from sensor data             |
| `signal_processing.py`  | Extracts SciPy-based statistical and frequency-domain vibration features |

Important extracted features include:

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

## `models/`

This folder contains machine learning scripts, trained model files, metadata, evaluation reports, and feature importance reports.

| File                            | Purpose                                                        |
| ------------------------------- | -------------------------------------------------------------- |
| `prepare_real_ims_data.py`      | Processes raw NASA IMS vibration data into training CSV format |
| `train_real_model.py`           | Trains the RandomForestClassifier using real NASA IMS data     |
| `predict_real_model.py`         | Loads the trained real model and performs prediction           |
| `evaluate_real_model.py`        | Evaluates the trained real model                               |
| `feature_importance_real.py`    | Generates feature importance report for the trained model      |
| `trained_model_real.pkl`        | Saved real-data trained RandomForestClassifier model           |
| `model_metadata_real.json`      | Metadata for the trained real model                            |
| `evaluation_report_real.json`   | Saved evaluation report for the real model                     |
| `feature_importance_real.json`  | Saved feature importance report                                |
| `test_real_model_prediction.py` | Manual script for testing real model prediction                |

## `data/`

This folder contains processed data and local raw dataset files.

| Path                          | Purpose                                                          |
| ----------------------------- | ---------------------------------------------------------------- |
| `data/training_data_real.csv` | Processed NASA IMS training dataset used for real model training |
| `data/raw/`                   | Local raw NASA IMS dataset folder                                |

Important:

```text
data/raw/
```

is ignored by Git because the raw NASA IMS dataset is large.

## `database/`

This folder contains database connection and prediction storage logic.

| File    | Purpose                                                                                               |
| ------- | ----------------------------------------------------------------------------------------------------- |
| `db.py` | Connects to PostgreSQL, creates prediction table, saves predictions, and retrieves prediction history |

The database stores:

* machine ID
* raw sensor data
* extracted features
* risk level
* failure probability
* recommended action
* anomaly detection result
* timestamp

## `producer/`

This folder contains Kafka producer logic.

The Kafka producer sends simulated machine sensor readings to the Kafka topic.

Kafka topic:

```text
machine.sensor.raw
```

## `consumer/`

This folder contains Kafka consumer logic.

The Kafka consumer listens to Kafka sensor messages and sends them to the FastAPI `/predict` endpoint.

## `tests/`

This folder contains automated tests for the H2 component.

Tests verify:

* API endpoints
* prediction logic
* machine learning model integration
* feature extraction
* SciPy signal processing
* anomaly detection
* real NASA IMS processed dataset
* real NASA IMS trained model
* feature importance report

Current expected test result:

```text
26 passed
```

## Overall Structure Summary

```text
h2-data-intelligence/
├── api/
├── consumer/
├── data/
├── database/
├── features/
├── models/
├── producer/
├── tests/
├── README.md
├── SETUP.md
├── ARCHITECTURE.md
├── VIVA_NOTES.md
├── DEMO_GUIDE.md
├── DATASET.md
├── MODEL_CARD.md
├── PROJECT_STRUCTURE.md
├── .env.example
├── .gitignore
├── docker-compose.yml
└── requirements.txt
```

## Why This Structure Is Useful

The project is separated into clear modules:

* API logic is inside `api/`
* Feature extraction is inside `features/`
* Machine learning logic is inside `models/`
* Database logic is inside `database/`
* Kafka streaming logic is inside `producer/` and `consumer/`
* Tests are inside `tests/`
* Documentation is stored as separate Markdown files

This makes the project easier to maintain, test, explain, and extend.
