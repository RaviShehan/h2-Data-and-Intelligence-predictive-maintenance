# H2 Data Intelligence Architecture

This document explains the architecture of the H2 Data and Intelligence component of the Group H Predictive Maintenance System.

## Purpose of H2

H2 is responsible for receiving machine sensor data, extracting useful features, predicting machine health risk, detecting abnormal sensor behavior, and storing prediction results.

The main goal of H2 is to convert raw machine sensor readings into meaningful predictive maintenance insights.

## High-Level System Flow

```text
Sensor Simulator
      ↓
Kafka Producer
      ↓
Kafka Topic
      ↓
Kafka Consumer
      ↓
FastAPI Prediction API
      ↓
Feature Extraction
      ↓
SciPy Signal Processing
      ↓
RandomForestClassifier Model
      ↓
Anomaly Detection
      ↓
PostgreSQL Database