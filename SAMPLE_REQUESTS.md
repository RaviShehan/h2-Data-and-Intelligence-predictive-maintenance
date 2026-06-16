# H2 Data Intelligence Sample API Requests

This document contains sample API requests for testing the H2 Data Intelligence FastAPI endpoints.

Base URL:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 1. Health Check

### Endpoint

```http
GET /
```

### curl Request

```bash
curl http://127.0.0.1:8000/
```

### Expected Response

```json
{
  "message": "H2 Predictive Maintenance API is running"
}
```

## 2. Predict Machine Risk - Normal Example

### Endpoint

```http
POST /predict
```

### curl Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" ^
-H "Content-Type: application/json" ^
-d "{\"machine_id\":\"MACHINE_01\",\"temperature\":45,\"vibration_x\":0.3,\"vibration_y\":0.2,\"vibration_z\":0.4,\"rpm\":1450}"
```

### Example Request Body

```json
{
  "machine_id": "MACHINE_01",
  "temperature": 45,
  "vibration_x": 0.3,
  "vibration_y": 0.2,
  "vibration_z": 0.4,
  "rpm": 1450
}
```

## 3. Predict Machine Risk - Warning or Critical Example

### Endpoint

```http
POST /predict
```

### Example Request Body

```json
{
  "machine_id": "MACHINE_02",
  "temperature": 78,
  "vibration_x": 1.4,
  "vibration_y": 1.2,
  "vibration_z": 1.3,
  "rpm": 1600
}
```

This request can produce higher risk because the vibration and temperature values are higher.

## 4. Predict Machine Risk - Anomaly Example

### Endpoint

```http
POST /predict
```

### Example Request Body

```json
{
  "machine_id": "MACHINE_03",
  "temperature": 90,
  "vibration_x": 2.5,
  "vibration_y": 2.2,
  "vibration_z": 2.1,
  "rpm": 6000
}
```

This request should trigger anomaly detection because:

* temperature is very high
* vibration is abnormal
* rpm is too high

Expected anomaly section:

```json
{
  "anomaly_detection": {
    "is_anomaly": true,
    "anomaly_reasons": [
      "Very high temperature detected",
      "Abnormal vibration level detected",
      "RPM too high for normal operation"
    ]
  }
}
```

## 5. View Prediction History

### Endpoint

```http
GET /predictions
```

### curl Request

```bash
curl http://127.0.0.1:8000/predictions
```

This returns recently stored prediction records from PostgreSQL.

## 6. View Model Information

### Endpoint

```http
GET /model-info
```

### curl Request

```bash
curl http://127.0.0.1:8000/model-info
```

This returns:

* model name
* model type
* dataset source
* input features
* risk classes
* accuracy
* model availability

## 7. View Model Evaluation

### Endpoint

```http
GET /model-evaluation
```

### curl Request

```bash
curl http://127.0.0.1:8000/model-evaluation
```

This returns:

* model type
* dataset source
* accuracy
* classification report
* confusion matrix

## 8. View Feature Importance

### Endpoint

```http
GET /feature-importance
```

### curl Request

```bash
curl http://127.0.0.1:8000/feature-importance
```

This returns the feature importance report for the real NASA IMS RandomForestClassifier model.

## 9. Invalid Input Example

### Endpoint

```http
POST /predict
```

### Example Request Body

```json
{
  "machine_id": "",
  "temperature": 150,
  "vibration_x": 10,
  "vibration_y": 1.0,
  "vibration_z": 1.1,
  "rpm": 12000
}
```

This request should fail validation because:

* machine_id is empty
* temperature is too high
* vibration_x is too high
* rpm is too high

## Viva Explanation

During viva, these sample requests can be used to demonstrate the API endpoints quickly. The `/predict` endpoint shows feature extraction, SciPy signal processing, real NASA IMS model prediction, anomaly detection, and PostgreSQL storage in one request.
