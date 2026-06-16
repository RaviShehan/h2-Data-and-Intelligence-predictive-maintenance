# H2 Data Intelligence Requirements

This document explains the functional and non-functional requirements of the H2 Data and Intelligence component.

## 1. Purpose

The purpose of H2 is to process machine sensor data and generate predictive maintenance insights.

H2 receives machine sensor readings, extracts useful features, predicts machine health risk, detects abnormal sensor behavior, stores prediction history, and exposes results through API endpoints.

## 2. Functional Requirements

### FR1: Receive Machine Sensor Data

The system shall receive machine sensor readings containing:

* machine_id
* temperature
* vibration_x
* vibration_y
* vibration_z
* rpm

### FR2: Validate Sensor Data

The system shall validate incoming sensor values before prediction.

Validation rules:

* machine_id cannot be empty
* temperature must be between 0 and 120
* vibration_x must be between 0 and 5
* vibration_y must be between 0 and 5
* vibration_z must be between 0 and 5
* rpm must be between 0 and 10000

### FR3: Extract Basic Vibration Features

The system shall extract vibration features from raw vibration readings.

Extracted features include:

* vibration_total
* vibration_rms
* vibration_mean
* vibration_peak
* vibration_std

### FR4: Extract SciPy Signal Features

The system shall extract statistical and frequency-domain signal features using NumPy and SciPy.

Extracted signal features include:

* signal_rms
* signal_mean
* signal_peak
* signal_std
* signal_skewness
* signal_kurtosis
* spectral_energy

### FR5: Predict Machine Health Risk

The system shall use a trained RandomForestClassifier model to predict machine health risk.

The model shall predict one of:

* NORMAL
* WARNING
* CRITICAL

### FR6: Return Prediction Probability

The system shall return prediction probabilities for each risk class.

Example risk classes:

* NORMAL
* WARNING
* CRITICAL

### FR7: Recommend Maintenance Action

The system shall return a recommended action based on predicted risk level.

Examples:

* Machine operating normally
* Schedule inspection soon
* Immediate maintenance required

### FR8: Detect Sensor Anomalies

The system shall detect abnormal sensor behavior using threshold-based anomaly detection.

Detected anomalies may include:

* very high temperature
* abnormal vibration level
* very low rpm
* very high rpm

### FR9: Store Prediction History

The system shall store prediction results in PostgreSQL.

Stored data shall include:

* machine ID
* raw sensor data
* extracted features
* predicted risk level
* failure probability
* recommended action
* anomaly detection result
* timestamp

### FR10: Provide API Endpoints

The system shall provide FastAPI endpoints for:

* health check
* machine risk prediction
* prediction history
* model information
* model evaluation
* feature importance

Main endpoints:

* `GET /`
* `POST /predict`
* `GET /predictions`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`

### FR11: Support Kafka Streaming

The system shall support Kafka-based sensor data streaming.

The Kafka producer shall send sensor readings to a Kafka topic.

The Kafka consumer shall receive sensor readings and send them to the FastAPI prediction endpoint.

### FR12: Provide Model Metadata

The system shall provide model lifecycle metadata through the `/model-info` endpoint.

Metadata includes:

* model name
* model type
* dataset source
* training dataset
* input features
* risk classes
* accuracy
* model file availability

### FR13: Provide Model Evaluation Report

The system shall provide model evaluation results through the `/model-evaluation` endpoint.

Evaluation data includes:

* accuracy
* classification report
* confusion matrix

### FR14: Provide Feature Importance Report

The system shall provide feature importance results through the `/feature-importance` endpoint.

This helps explain which vibration and signal-processing features are most important for prediction.

## 3. Non-Functional Requirements

### NFR1: Reliability

The system should be tested using automated pytest tests.

Current expected test result:

```text
26 passed
```

### NFR2: Maintainability

The project should be separated into clear modules:

* API logic
* feature extraction
* signal processing
* machine learning
* database logic
* Kafka producer
* Kafka consumer
* tests
* documentation

### NFR3: Explainability

The system should provide model metadata, model evaluation, and feature importance so that predictions can be explained during viva and report writing.

### NFR4: Security

Sensitive values such as database passwords should be stored in `.env`.

The `.env` file should not be pushed to GitHub.

A safe `.env.example` file should be provided.

### NFR5: Data Safety

The raw NASA IMS dataset should not be uploaded to GitHub.

The raw dataset folder should be ignored:

```text
data/raw/
```

### NFR6: Usability

The project should provide documentation files such as:

* README.md
* SETUP.md
* API_REFERENCE.md
* DEMO_GUIDE.md
* VIVA_NOTES.md
* TROUBLESHOOTING.md

These documents help users set up, run, test, and explain the project.

### NFR7: Local Development Support

The system should be runnable locally using:

* Python virtual environment
* FastAPI
* PostgreSQL
* Docker
* Kafka

### NFR8: Testability

The system should include tests for:

* API endpoints
* validation
* feature extraction
* SciPy signal processing
* anomaly detection
* real NASA IMS model prediction
* real dataset structure
* feature importance report

## 4. System Constraints

Current constraints:

* The system is currently designed for local development.
* The raw NASA IMS dataset is stored locally and not pushed to GitHub.
* The current model uses the `2nd_test` subset of the NASA IMS dataset.
* Authentication is not implemented yet.
* Dashboard integration is handled by another group component.

## 5. Future Requirements

Future improvements may include:

* Train using all NASA IMS test sets
* Add MLflow model tracking
* Add dashboard integration
* Add alert notifications
* Add API authentication
* Deploy using Docker or cloud infrastructure
* Add production monitoring
* Improve labeling using real failure timestamps
