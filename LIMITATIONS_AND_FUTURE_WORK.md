# H2 Data Intelligence Limitations and Future Work

This document explains the current limitations of the H2 Data and Intelligence component and possible future improvements.

## 1. Current Limitations

### 1.1 Local Development Only

The current system is designed to run locally on a developer machine.

It uses:

* local FastAPI server
* local PostgreSQL database
* local Docker Kafka container
* local raw NASA IMS dataset

The system is not yet deployed to a cloud or production environment.

### 1.2 Limited NASA IMS Dataset Usage

The current model uses the `2nd_test` subset of the NASA IMS Bearing Dataset.

This is enough to prove real dataset integration, but using all available IMS test sets could improve model generalization.

### 1.3 Labeling Method

The current labels are assigned based on time progression.

The dataset is treated as:

* earlier period = NORMAL
* middle period = WARNING
* later period = CRITICAL

This is a practical approach for this project, but future work can improve labeling using exact failure timestamps or domain expert rules.

### 1.4 No Authentication

The current FastAPI endpoints are open locally.

There is no login system, API key, or role-based access control.

This is acceptable for a local university prototype, but production systems should include authentication.

### 1.5 No Dashboard in H2

H2 focuses on the Data and Intelligence layer.

Dashboard visualization is expected to be handled by another group component.

H2 provides APIs and stored prediction data that can be used by dashboard teams.

### 1.6 No Real Sensor Hardware Integration

The current system uses simulated sensor data and real historical NASA IMS vibration data.

It is not directly connected to real-time physical machine sensors yet.

### 1.7 No Production Monitoring

The system does not yet include production-level monitoring tools such as:

* API request monitoring
* model drift detection
* alert monitoring
* uptime monitoring
* centralized logging

### 1.8 No MLflow Model Tracking

The current project stores model metadata manually using JSON files.

MLflow or another model tracking tool could be added later for better model version management.

## 2. Future Improvements

### 2.1 Train Using All NASA IMS Test Sets

The model can be improved by using all available IMS dataset test sets instead of only `2nd_test`.

This may improve model robustness and generalization.

### 2.2 Improve Labeling Method

Future work can improve the labeling strategy using:

* actual failure timestamps
* bearing degradation stages
* domain expert thresholds
* unsupervised anomaly detection
* remaining useful life estimation

### 2.3 Add MLflow Model Tracking

MLflow can be added to track:

* model versions
* training parameters
* accuracy scores
* datasets used
* model artifacts

This would make the machine learning lifecycle more professional.

### 2.4 Add Dashboard Integration

A dashboard can be connected to H2 APIs to visualize:

* latest machine health status
* prediction history
* anomaly alerts
* failure probability trends
* model evaluation results
* feature importance

### 2.5 Add Alert Notifications

The system can be extended to send alerts when CRITICAL risk or anomaly is detected.

Possible alert methods:

* email
* SMS
* dashboard notification
* Slack or Teams message

### 2.6 Add API Authentication

Security can be improved by adding:

* API keys
* JWT authentication
* user login
* role-based access control

### 2.7 Deploy the System

The system can be deployed using:

* Docker
* cloud virtual machine
* Kubernetes
* managed PostgreSQL
* managed Kafka service

### 2.8 Add Model Drift Monitoring

In real predictive maintenance systems, machine behavior can change over time.

Future work can include model drift detection to identify when the model needs retraining.

### 2.9 Add More Advanced Models

Future model improvements can include:

* XGBoost
* LightGBM
* neural networks
* LSTM models for time-series data
* autoencoders for anomaly detection
* remaining useful life prediction models

### 2.10 Improve Real-Time Pipeline

The Kafka pipeline can be improved by adding:

* retry handling
* dead-letter queues
* message schema validation
* better error logging
* consumer group scaling

## 3. Viva Explanation

During viva, limitations and future work can be explained like this:

The current H2 component is a strong local prototype. It uses real NASA IMS vibration data, SciPy signal processing, RandomForestClassifier prediction, anomaly detection, Kafka streaming simulation, PostgreSQL storage, feature importance, and automated tests. However, it is not yet a production system. Future improvements include using all IMS datasets, improving labels using real failure timestamps, adding MLflow, adding authentication, connecting a dashboard, adding alerts, and deploying the system.
