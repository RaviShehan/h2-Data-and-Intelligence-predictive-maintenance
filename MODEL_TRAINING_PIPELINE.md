# H2 Data Intelligence Model Training Pipeline

This document explains how the H2 Data and Intelligence component prepares data, trains the machine learning model, evaluates it, and generates feature importance.

## 1. Pipeline Overview

The model training pipeline converts raw NASA IMS Bearing Dataset vibration files into a trained predictive maintenance model.

```text
Raw NASA IMS Vibration Files
      ↓
Data Preprocessing
      ↓
Feature Extraction
      ↓
SciPy Signal Processing
      ↓
Processed Training CSV
      ↓
RandomForestClassifier Training
      ↓
Model Evaluation
      ↓
Feature Importance Generation
      ↓
FastAPI Model Integration
```

## 2. Raw Dataset

The raw NASA IMS Bearing Dataset is stored locally inside:

```text
data/raw/
```

This folder is ignored by Git because the raw dataset is large.

The project currently uses the `2nd_test` subset of the NASA IMS dataset.

## 3. Data Preprocessing

Preprocessing script:

```text
models/prepare_real_ims_data.py
```

Run preprocessing:

```bash
venv\Scripts\python.exe -m models.prepare_real_ims_data
```

This script:

* reads raw NASA IMS vibration files
* extracts vibration values
* calculates basic vibration features
* extracts SciPy signal-processing features
* assigns risk labels
* creates a processed CSV file

Output file:

```text
data/training_data_real.csv
```

## 4. Extracted Features

The training dataset contains vibration and signal-processing features.

Basic vibration features:

* vibration_total
* vibration_rms
* vibration_mean
* vibration_peak
* vibration_std

SciPy signal-processing features:

* signal_rms
* signal_mean
* signal_peak
* signal_std
* signal_skewness
* signal_kurtosis
* spectral_energy

These features are used as input to the machine learning model.

## 5. Labeling Method

The current project assigns machine health labels based on time progression.

The labels are:

* NORMAL
* WARNING
* CRITICAL

General labeling idea:

```text
Early data period   → NORMAL
Middle data period  → WARNING
Late data period    → CRITICAL
```

This is suitable for the current university prototype because bearing datasets usually show degradation over time.

Future work can improve labeling using real failure timestamps or domain expert rules.

## 6. Model Training

Training script:

```text
models/train_real_model.py
```

Run training:

```bash
venv\Scripts\python.exe models/train_real_model.py
```

The system trains a:

```text
RandomForestClassifier
```

Generated files:

```text
models/trained_model_real.pkl
models/model_metadata_real.json
```

## 7. Model Metadata

The model metadata file stores information about the trained model.

Metadata file:

```text
models/model_metadata_real.json
```

It includes:

* model name
* model type
* model file path
* training dataset path
* dataset source
* training timestamp
* input features
* risk classes
* accuracy score

This metadata is exposed through:

```http
GET /model-info
```

## 8. Model Evaluation

Evaluation script:

```text
models/evaluate_real_model.py
```

Run evaluation:

```bash
venv\Scripts\python.exe models/evaluate_real_model.py
```

Generated file:

```text
models/evaluation_report_real.json
```

The evaluation report includes:

* model type
* dataset source
* accuracy
* classification report
* confusion matrix

Current real model accuracy:

```text
0.9645
```

This evaluation report is exposed through:

```http
GET /model-evaluation
```

## 9. Feature Importance

Feature importance script:

```text
models/feature_importance_real.py
```

Run feature importance generation:

```bash
venv\Scripts\python.exe models/feature_importance_real.py
```

Generated file:

```text
models/feature_importance_real.json
```

Feature importance explains which vibration and SciPy signal-processing features contribute most to the RandomForestClassifier prediction.

This report is exposed through:

```http
GET /feature-importance
```

## 10. FastAPI Integration

The trained model is used by the prediction API.

Main prediction endpoint:

```http
POST /predict
```

The prediction flow is:

```text
Sensor input
      ↓
Input validation
      ↓
Feature extraction
      ↓
SciPy signal feature extraction
      ↓
Real NASA IMS trained model prediction
      ↓
Anomaly detection
      ↓
PostgreSQL storage
      ↓
API response
```

## 11. Testing the Pipeline

Run all tests:

```bash
venv\Scripts\python.exe -m pytest tests
```

Expected result:

```text
26 passed
```

The tests verify:

* processed dataset structure
* real trained model prediction
* feature extraction
* SciPy signal processing
* model API integration
* feature importance report

## 12. Viva Explanation

During viva, the model training pipeline can be explained like this:

The system uses the NASA IMS Bearing Dataset as the real predictive maintenance dataset. Raw vibration files are processed into a training CSV by extracting vibration and SciPy signal-processing features. A RandomForestClassifier is trained using these features to classify machine health as NORMAL, WARNING, or CRITICAL. The model is evaluated, metadata is stored, feature importance is generated, and the trained model is integrated with FastAPI for real-time prediction.
