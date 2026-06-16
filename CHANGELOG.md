# Changelog

All important changes to the H2 Data Intelligence Predictive Maintenance System are documented here.

## Latest Version

### Added

* FastAPI prediction API
* Kafka producer for streaming machine sensor data
* Kafka consumer for receiving machine sensor data
* PostgreSQL prediction history storage
* `/predictions` endpoint for prediction history
* Feature extraction from temperature and vibration sensor readings
* SciPy-based signal processing features
* NASA IMS Bearing Dataset preprocessing
* Real-data RandomForestClassifier model training
* Model metadata generation
* Model evaluation report generation
* Feature importance report generation
* `/model-info` endpoint
* `/model-evaluation` endpoint
* `/feature-importance` endpoint
* Streaming anomaly detection
* API input validation
* Automated pytest test suite
* GitHub Actions automated test workflow
* GitHub Actions test badge in README
* Safe `.env.example` file
* Documentation files for setup, architecture, API reference, testing, security, troubleshooting, viva notes, demo guide, and final checklist

### Changed

* Improved model accuracy by adding SciPy-based statistical and frequency-domain vibration signal features
* Updated README with project documentation links
* Updated README with latest test count
* Updated model card with real NASA IMS model details
* Updated dataset documentation for NASA IMS dataset usage

### Current Test Result

```text
26 passed
```

### Current Model Accuracy

```text
0.9645
```

## Main Project Milestones

### 1. Initial API Development

Implemented the FastAPI backend for receiving machine sensor readings and returning machine risk predictions.

### 2. Kafka Streaming Integration

Added Kafka producer and consumer to simulate real-time machine sensor data streaming.

### 3. PostgreSQL Storage

Added PostgreSQL database integration to store prediction history.

### 4. Feature Extraction

Added vibration and temperature feature extraction.

Extracted features include:

* vibration_total
* vibration_rms
* vibration_mean
* vibration_peak
* vibration_std
* temperature_status

### 5. SciPy Signal Processing

Added statistical and frequency-domain signal features using NumPy and SciPy.

Signal features include:

* signal_rms
* signal_mean
* signal_peak
* signal_std
* signal_skewness
* signal_kurtosis
* spectral_energy

### 6. Real Dataset Integration

Integrated the NASA IMS Bearing Dataset for real predictive maintenance model training.

### 7. Real Machine Learning Model

Trained a RandomForestClassifier using processed NASA IMS vibration features.

Current model accuracy:

```text
0.9645
```

### 8. Model Explainability

Added feature importance generation and `/feature-importance` API endpoint.

### 9. Anomaly Detection

Added threshold-based anomaly detection for abnormal temperature, vibration, and rpm values.

### 10. Automated Testing

Added pytest tests for:

* API endpoints
* prediction logic
* feature extraction
* SciPy signal processing
* anomaly detection
* real NASA IMS model prediction
* real NASA IMS processed dataset
* feature importance report

Current test result:

```text
26 passed
```

### 11. GitHub Actions CI

Added GitHub Actions workflow to automatically run tests after pushing code.

### 12. Documentation

Added documentation files:

* README.md
* SETUP.md
* ARCHITECTURE.md
* PROJECT_STRUCTURE.md
* API_REFERENCE.md
* MODEL_CARD.md
* DATASET.md
* DEMO_GUIDE.md
* VIVA_NOTES.md
* TROUBLESHOOTING.md
* SECURITY.md
* TESTING.md
* CI_CD.md
* REQUIREMENTS.md
* LIMITATIONS_AND_FUTURE_WORK.md
* FINAL_CHECKLIST.md
* CHANGELOG.md
