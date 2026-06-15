# Dataset Documentation - NASA IMS Bearing Dataset

## Dataset Used

This project uses the NASA IMS Bearing Dataset for real predictive maintenance model training.

The dataset contains bearing vibration signal data collected during bearing degradation experiments.

## Purpose in This Project

The dataset is used to train a machine learning model that predicts machine health risk levels:

* NORMAL
* WARNING
* CRITICAL

The model uses vibration-based and SciPy-based signal-processing features extracted from raw bearing vibration signals.

## Raw Dataset Location

The raw dataset is stored locally in:

```text
data/raw/
```

This folder is ignored by Git because the raw dataset is large and should not be uploaded to GitHub.

## Extracted Dataset Used

For the current implementation, the project uses the `2nd_test` subset of the IMS dataset.

The extracted files are stored locally in:

```text
data/raw/IMS/extracted/2nd_test/2nd_test
```

## Processed Training Dataset

The raw vibration files are processed into a CSV file:

```text
data/training_data_real.csv
```

This processed file contains extracted vibration features, SciPy signal-processing features, and machine health labels.

## Preprocessing Script

The preprocessing script is:

```text
models/prepare_real_ims_data.py
```

This script performs the following steps:

* Reads raw vibration signal files
* Extracts vibration features
* Extracts SciPy-based signal-processing features
* Assigns machine health labels based on degradation progress
* Saves the processed dataset as `training_data_real.csv`

## Extracted Features

The following features are extracted from vibration signals:

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

The `signal_skewness` and `signal_kurtosis` features are extracted using SciPy.

The `spectral_energy` feature is extracted using FFT-based frequency-domain analysis.

## Labeling Method

The IMS dataset contains degradation over time. In this project, labels are assigned based on dataset progress:

* Early stage data → NORMAL
* Middle stage data → WARNING
* Late stage data → CRITICAL

This creates a supervised learning dataset for machine health risk classification.

## Model Training

The real-data model is trained using:

```text
models/train_real_model.py
```

The trained model is saved as:

```text
models/trained_model_real.pkl
```

Model metadata is saved as:

```text
models/model_metadata_real.json
```

## Model Evaluation

The real-data model is evaluated using:

```text
models/evaluate_real_model.py
```

The evaluation report is saved as:

```text
models/evaluation_report_real.json
```

Current model accuracy after adding SciPy signal-processing features:

```text
0.9645
```

## Current Limitation

The current version uses only the `2nd_test` subset of the NASA IMS dataset.

Future versions can improve the system by using all available IMS test sets:

* 1st_test
* 2nd_test
* 3rd_test

## Why Raw Data Is Not Uploaded

The raw NASA IMS dataset is large, so the project uses `.gitignore` to avoid uploading it to GitHub.

The `.gitignore` file contains:

```text
data/raw/
```
