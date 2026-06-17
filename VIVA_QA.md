# Predictive Maintenance System - Viva Questions and Answers

## 1. What is the main purpose of this project?

This project predicts the health condition of industrial machines using sensor data.

It uses temperature, vibration, and RPM readings to predict machine risk levels such as NORMAL, WARNING, and CRITICAL. The goal is to detect possible machine failure early and support predictive maintenance.

## 2. What are H1, H2, H3, and H4 in this system?

| Component | Responsibility                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------ |
| H1        | Edge device simulator that generates and validates sensor telemetry                                          |
| H2        | Data intelligence layer with API, feature extraction, ML prediction, anomaly detection, and database storage |
| H3        | Streamlit dashboard for visualizing predictions, model information, feature importance, and system health    |
| H4        | Platform monitoring, CI/CD, security practices, and system health checking                                   |

## 3. What does H1 do?

H1 simulates edge devices attached to machines.

It generates telemetry such as:

* machine_id
* temperature
* vibration_x
* vibration_y
* vibration_z
* rpm
* timestamp

It also performs edge-side filtering and validation before sending the data to Kafka.

## 4. Why did you use Kafka?

Kafka is used to simulate real-time data streaming between the edge layer and the backend system.

H1 sends sensor telemetry to a Kafka topic. H2 consumes that telemetry and sends it to the prediction API.

This makes the system closer to a real industrial IoT architecture.

## 5. What does H2 do?

H2 is the main data intelligence component.

It performs:

* input validation
* feature extraction
* SciPy signal processing
* machine learning prediction
* anomaly detection
* PostgreSQL storage
* API endpoint exposure

## 6. What machine learning model is used?

The system uses a RandomForestClassifier trained using processed NASA IMS bearing dataset features.

The model predicts the machine risk level based on extracted vibration and signal-processing features.

## 7. Why did you use the NASA IMS dataset?

NASA IMS is a real bearing degradation dataset used for predictive maintenance research.

Using this dataset makes the project more realistic than using only random artificial data.

## 8. What features are extracted from sensor data?

The system extracts features such as:

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

These features help the model understand machine vibration behavior.

## 9. Why did you use SciPy?

SciPy is used for signal-processing feature extraction.

It helps calculate statistical and signal-based features from vibration values. This improves the quality of the machine learning input.

## 10. What does anomaly detection do?

Anomaly detection checks whether sensor readings are abnormal.

For example, it can detect:

* very high temperature
* abnormal vibration
* very low RPM
* very high RPM

This provides an additional safety layer beside the ML model.

## 11. What does H3 dashboard show?

The H3 Streamlit dashboard shows:

* prediction history
* risk level summary
* anomaly summary
* model information
* model evaluation
* feature importance
* H4 system health status

## 12. What does H4 system health monitoring do?

H4 provides the `/system-health` endpoint.

It checks:

* API status
* database connection status
* model file availability
* evaluation report availability
* feature importance report availability

This helps verify whether the platform is running correctly.

## 13. What database is used?

The project uses PostgreSQL.

Prediction results are stored in the database so that past machine health records can be viewed later through the API and dashboard.

## 14. What API framework is used?

The project uses FastAPI.

FastAPI is used because it is fast, simple, supports validation, and automatically provides Swagger documentation.

## 15. What endpoints are available?

Important endpoints include:

* `GET /`
* `POST /predict`
* `GET /predictions`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`
* `GET /system-health`

## 16. How do you test the project?

The project uses pytest.

The tests verify:

* H1 edge simulator
* API endpoints
* feature extraction
* SciPy signal processing
* anomaly detection
* real model prediction
* real dataset structure
* feature importance report
* H3 dashboard utility logic
* H4 system health monitoring

The current test suite gives 35 passed tests.

## 17. What is CI/CD in this project?

GitHub Actions is used for CI/CD.

Every push runs automated tests. If the tests pass, the workflow becomes green. This proves that new changes did not break the system.

## 18. How is security handled?

Security practices include:

* `.env` file for secrets
* `.env.example` for safe configuration sharing
* `.gitignore` to avoid uploading raw data and secrets
* validation of API input values
* documentation of security practices

## 19. What is the full system flow?

The full flow is:

```text
H1 Edge Device Simulator
        ↓
Kafka Topic
        ↓
H2 Kafka Consumer
        ↓
FastAPI Prediction API
        ↓
Feature Extraction
        ↓
Machine Learning Model
        ↓
Anomaly Detection
        ↓
PostgreSQL Database
        ↓
H3 Dashboard
        ↓
H4 System Health Monitoring
```

## 20. What is the strongest part of this project?

The strongest part is that the project is not just a simple ML model.

It includes a full end-to-end architecture with edge simulation, Kafka streaming, FastAPI backend, real dataset model training, PostgreSQL storage, Streamlit dashboard, system health monitoring, automated testing, and GitHub Actions CI/CD.

## Final Viva Summary

This project is an end-to-end predictive maintenance system. H1 generates validated edge telemetry and sends it through Kafka. H2 receives the data, extracts vibration and signal-processing features, predicts machine risk using a real NASA IMS trained RandomForestClassifier model, detects anomalies, and stores results in PostgreSQL. H3 visualizes prediction history, risk summary, model details, feature importance, and system health. H4 adds system monitoring, CI/CD, and security practices. The system is tested using pytest with 35 passing tests and GitHub Actions.
