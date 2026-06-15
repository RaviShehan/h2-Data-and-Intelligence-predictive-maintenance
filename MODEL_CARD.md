# Model Card - NASA IMS Bearing Risk Prediction Model

## Model Overview

This model is used in the H2 Data Intelligence component of the Predictive Maintenance System.

The model predicts machine health risk using vibration features extracted from the NASA IMS Bearing Dataset.

## Model Type

* RandomForestClassifier

## Dataset

The model is trained using the NASA IMS Bearing Dataset.

The raw dataset contains bearing vibration signal files collected during bearing degradation experiments.

In this project, the raw vibration files are processed into:

```text
data/training_data_real.csv
```

The raw dataset folder is ignored by Git:

```text
data/raw/
```

## Input Features

The model uses the following vibration-based features:

* vibration_total
* vibration_rms
* vibration_mean
* vibration_peak
* vibration_std

## Output Classes

The model predicts one of the following machine health states:

* NORMAL
* WARNING
* CRITICAL

## Model Performance

Current real-data model accuracy:

```text
0.9289
```

The model evaluation report is saved in:

```text
models/evaluation_report_real.json
```

## Model Files

* `models/train_real_model.py`
* `models/predict_real_model.py`
* `models/trained_model_real.pkl`
* `models/model_metadata_real.json`
* `models/evaluate_real_model.py`
* `models/evaluation_report_real.json`

## API Integration

The trained model is integrated with the FastAPI `/predict` endpoint.

The API response includes:

* predicted risk level
* failure probability
* prediction probabilities for each class
* dataset source
* recommended action

## Limitations

* The current real-data model uses only the `2nd_test` subset of the NASA IMS dataset.
* The labels NORMAL, WARNING, and CRITICAL are assigned based on degradation progress.
* Temperature and RPM are used in the API pipeline, but the real NASA IMS model mainly uses vibration features.
* Future versions can improve accuracy and realism by using all IMS test sets and more advanced signal processing.

## Future Improvements

* Train using all IMS test sets
* Add MLflow model tracking
* Add SciPy-based frequency-domain features
* Add model versioning
* Add dashboard visualization for model predictions
