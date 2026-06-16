# H2 Data Intelligence Testing Guide

This document explains the automated tests used in the H2 Data and Intelligence component.

## Purpose of Testing

Testing is used to verify that the system works correctly after changes.

The tests check:

* API endpoints
* input validation
* feature extraction
* SciPy signal processing
* anomaly detection
* real NASA IMS model prediction
* real NASA IMS processed dataset
* feature importance report

## Run All Tests

Run this command from the project root:

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
26 passed
```

## Test Folder

All automated tests are stored inside:

```text
tests/
```

## Main Test Areas

### 1. API Endpoint Tests

These tests verify that FastAPI endpoints work correctly.

They test endpoints such as:

* `GET /`
* `POST /predict`
* `GET /model-info`
* `GET /model-evaluation`
* `GET /feature-importance`

Important file:

```text
tests/test_api_endpoints.py
```

### 2. Feature Extraction Tests

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

### 3. SciPy Signal Processing Tests

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

### 4. Anomaly Detection Tests

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

### 5. Real NASA IMS Model Tests

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

### 6. Real Dataset Tests

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

### 7. Feature Importance Tests

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

## Why These Tests Are Important

These tests prove that the H2 component is not only implemented, but also verified.

The tests show that:

* the API works
* the machine learning model is connected
* real NASA IMS data is used
* feature extraction works
* SciPy signal processing works
* anomaly detection works
* feature importance explainability works
* documentation and implementation are supported by automated checks

## Viva Explanation

During viva, testing can be explained like this:

The project includes automated pytest tests to verify the API endpoints, feature extraction, SciPy signal processing, anomaly detection, real NASA IMS model integration, dataset structure, and feature importance report. The current test suite gives 26 passed tests, which proves that the main H2 functionality is working correctly.
