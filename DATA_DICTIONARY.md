# H2 Data Intelligence Data Dictionary

This document explains the main data fields used in the H2 Data and Intelligence component.

## 1. Raw Sensor Input Fields

These fields are received by the FastAPI `/predict` endpoint.

| Field       | Type    | Description                      |
| ----------- | ------- | -------------------------------- |
| machine_id  | string  | Unique identifier of the machine |
| temperature | float   | Machine temperature reading      |
| vibration_x | float   | Vibration reading in X direction |
| vibration_y | float   | Vibration reading in Y direction |
| vibration_z | float   | Vibration reading in Z direction |
| rpm         | integer | Machine rotation speed           |

## 2. Input Validation Rules

| Field       | Validation Rule             |
| ----------- | --------------------------- |
| machine_id  | Cannot be empty             |
| temperature | Must be between 0 and 120   |
| vibration_x | Must be between 0 and 5     |
| vibration_y | Must be between 0 and 5     |
| vibration_z | Must be between 0 and 5     |
| rpm         | Must be between 0 and 10000 |

Validation logic is implemented in:

```text
api/validation.py
```

## 3. Basic Extracted Features

These features are extracted from the raw sensor readings before prediction.

| Feature            | Description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| vibration_total    | Total vibration magnitude calculated from X, Y, and Z vibration values |
| vibration_rms      | Root mean square value of vibration readings                           |
| vibration_mean     | Mean value of vibration readings                                       |
| vibration_peak     | Maximum vibration value                                                |
| vibration_std      | Standard deviation of vibration readings                               |
| temperature_status | Categorized temperature condition                                      |

Feature extraction logic is implemented in:

```text
features/feature_extraction.py
```

## 4. SciPy Signal Processing Features

These features are extracted using NumPy and SciPy.

| Feature         | Description                                                     |
| --------------- | --------------------------------------------------------------- |
| signal_rms      | Root mean square value of the vibration signal                  |
| signal_mean     | Mean value of the vibration signal                              |
| signal_peak     | Maximum absolute signal value                                   |
| signal_std      | Standard deviation of the signal                                |
| signal_skewness | Measures asymmetry of the vibration signal distribution         |
| signal_kurtosis | Measures the sharpness or peakedness of the signal distribution |
| spectral_energy | Frequency-domain energy calculated using FFT                    |

Signal processing logic is implemented in:

```text
features/signal_processing.py
```

## 5. Machine Learning Input Features

The real NASA IMS trained RandomForestClassifier model uses the following input features:

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

These features are used by:

```text
models/predict_real_model.py
```

## 6. Model Output Fields

The machine learning model returns prediction information.

| Field               | Description                             |
| ------------------- | --------------------------------------- |
| machine_id          | Machine identifier                      |
| risk_level          | Predicted machine health risk           |
| failure_probability | Probability of the predicted risk class |
| recommended_action  | Suggested maintenance action            |
| model_type          | Type of machine learning model used     |
| dataset_source      | Dataset used for training               |
| probabilities       | Probability values for all risk classes |

## 7. Risk Levels

The model predicts one of three risk levels.

| Risk Level | Meaning                                |
| ---------- | -------------------------------------- |
| NORMAL     | Machine is operating normally          |
| WARNING    | Machine may need inspection soon       |
| CRITICAL   | Machine may need immediate maintenance |

## 8. Recommended Actions

| Risk Level | Recommended Action             |
| ---------- | ------------------------------ |
| NORMAL     | Machine operating normally     |
| WARNING    | Schedule inspection soon       |
| CRITICAL   | Immediate maintenance required |

## 9. Anomaly Detection Fields

The anomaly detection result is returned with each prediction.

| Field           | Description                                         |
| --------------- | --------------------------------------------------- |
| is_anomaly      | Shows whether abnormal sensor behavior was detected |
| anomaly_reasons | List of reasons for anomaly detection               |

Possible anomaly reasons:

* Very high temperature detected
* Abnormal vibration level detected
* RPM too low for normal operation
* RPM too high for normal operation

Anomaly detection logic is implemented in:

```text
api/anomaly.py
```

## 10. Database Fields

Prediction results are stored in the PostgreSQL `predictions` table.

| Database Column     | Description                                   |
| ------------------- | --------------------------------------------- |
| id                  | Unique prediction record ID                   |
| machine_id          | Machine identifier                            |
| temperature         | Machine temperature reading                   |
| vibration_total     | Total vibration value                         |
| rpm                 | Machine rotation speed                        |
| risk_level          | Predicted risk level                          |
| failure_probability | Probability of predicted class                |
| recommended_action  | Suggested maintenance action                  |
| sensor_data         | Original raw sensor input stored as JSONB     |
| features            | Extracted features stored as JSONB            |
| is_anomaly          | Whether anomaly was detected                  |
| anomaly_reasons     | Reasons for anomaly detection stored as JSONB |
| created_at          | Time prediction was stored                    |

Database logic is implemented in:

```text
database/db.py
```

## 11. Dataset Fields

The processed NASA IMS training dataset is stored in:

```text
data/training_data_real.csv
```

Important columns include:

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
* risk_level

## 12. Viva Explanation

During viva, the data dictionary can be explained like this:

The system receives raw machine sensor readings such as temperature, vibration, and rpm. These raw values are converted into basic vibration features and SciPy signal-processing features. The trained RandomForestClassifier uses these features to predict machine health risk. The prediction result, anomaly result, raw sensor data, and extracted features are stored in PostgreSQL for later monitoring.
