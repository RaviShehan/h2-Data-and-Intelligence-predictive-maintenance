# H1-H4 Predictive Maintenance System Testing Guide

This document explains the automated tests used in the Group H Predictive Maintenance System.

## Purpose of Testing

Testing is used to verify that the system works correctly after changes.

The tests check:

* H1 edge simulator
* API endpoints
* input validation
* feature extraction
* SciPy signal processing
* anomaly detection
* real NASA IMS model prediction
* real NASA IMS processed dataset
* feature importance report
* H3 dashboard prediction data normalization
* H4 system health monitoring endpoint

## Run All Tests

Run this command from the project root:

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
35 passed
```

## Test Folder

All automated tests are stored inside:

```text
tests/
```

## Main Test Areas

### 1. H1 Edge Simulator Tests

These tests verify the H1 edge simulator.

They check:

* raw sensor data generation
* required telemetry fields
* edge-side filtering and rounding
* valid telemetry acceptance
* invalid telemetry rejection

Important file:

```text
tests/test_edge_simulator.py
```

These tests prove that the H1 edge component can generate, filter, and validate machine telemetry before sending it to Kafka.

### 2. API Endpoint Tests

These tests verify that FastAPI endpoints work correctly.

They test endpoints such as:

* `GET /`
* `POST /predict`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`
* `GET /system-health`

Important file:

```text
tests/test_api_endpoints.py
```

These tests prove that the H2 and H4 API endpoints are working correctly.

### 3. Feature Extraction Tests

These tests verify that raw sensor readings are converted into useful features.

They check features such as:

* vibration_total
* vibration_rms
* vibration_mean
* vibration_peak
* vibration_std
* temperature_status

Important file:

```text
tests/test_feature_extraction.py
```

### 4. SciPy Signal Processing Tests

These tests verify statistical and frequency-domain feature extraction.

They check features such as:

* signal_rms
* signal_mean
* signal_peak
* signal_std
* signal_skewness
* signal_kurtosis
* spectral_energy

Important file:

```text
tests/test_signal_processing.py
```

These tests prove that SciPy-based vibration signal processing is working correctly.

### 5. Anomaly Detection Tests

These tests verify that abnormal sensor behavior is detected correctly.

They check conditions such as:

* very high temperature
* abnormal vibration level
* very low rpm
* very high rpm

Important file:

```text
tests/test_anomaly.py
```

### 6. Real NASA IMS Model Tests

These tests verify that the real trained RandomForestClassifier model can make predictions.

The tests confirm that the model returns:

* model type
* dataset source
* risk level
* failure probability
* prediction probabilities

Important file:

```text
tests/test_real_model.py
```

### 7. Real Dataset Tests

These tests verify that the processed NASA IMS dataset exists and has the required structure.

They check:

* dataset file existence
* required feature columns
* risk level column
* valid risk classes

Important file:

```text
tests/test_real_dataset.py
```

### 8. Feature Importance Tests

These tests verify that the feature importance report exists and contains required values.

They check:

* feature importance JSON file existence
* model type
* dataset source
* feature importance list
* SciPy features in the report

Important file:

```text
tests/test_feature_importance.py
```

### 9. H4 System Health Monitoring Test

This test verifies the H4 platform monitoring endpoint.

It checks that `/system-health` returns:

* system name
* overall status
* API status
* database status
* model file availability
* evaluation report availability
* feature importance report availability

Important file:

```text
tests/test_api_endpoints.py
```

This proves that H4 monitoring is connected to the backend API.

### 10. H3 Dashboard Utility Tests

These tests verify the H3 dashboard data-cleaning logic.

They check:

* prediction response from dictionary format
* prediction response from list format
* prediction response from JSON string format
* invalid JSON string handling

Important file:

```text
tests/test_dashboard_utils.py
```

These tests prove that the dashboard can safely normalize prediction data before displaying it in Streamlit.

## What the Tests Prove

These tests prove that the system is not tests prove that the dashboard can safely normalize prediction data before displaying it in Streamlit.

## What the Tests Prove

These tests prove that the system is not only implemented, but also verified.

The tests show that:

* H1 edge simulator works
* the API works
* the machine learning model is connected
* real NASA IMS data is used
* feature extraction works
* SciPy signal processing works
* anomaly detection works
* feature importance explainability works
* H3 dashboard utility logic works
* H4 system health monitoring works
* documentation and implementation are supported by automated checks

## Current Expected Result

The current expected test result is:

```text
35 passed
```

## Viva Explanation

During viva, testing can be explained like this:

The project includes automated pytest tests to verify the H1 edge simulator, FastAPI endpoints, feature extraction, SciPy signal processing, anomaly detection, real NASA IMS model integration, dataset structure, feature importance report, H3 dashboard utility logic, and H4 system health monitoring. The current test suite gives 35 passed tests, which proves that the main H1-H4 functionality is working correctly.
