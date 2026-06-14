import os

import psycopg2
from psycopg2.extras import Json, RealDictCursor
from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "h2_predictive_maintenance")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")

if DB_PASSWORD is None:
    raise ValueError("DB_PASSWORD is missing. Add it to your .env file.")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            machine_id VARCHAR(50) NOT NULL,
            temperature DOUBLE PRECISION NOT NULL,
            vibration_total DOUBLE PRECISION NOT NULL,
            rpm INTEGER NOT NULL,
            risk_level VARCHAR(20) NOT NULL,
            failure_probability DOUBLE PRECISION NOT NULL,
            recommended_action TEXT NOT NULL,
            sensor_data JSONB NOT NULL,
            features JSONB NOT NULL,
            is_anomaly BOOLEAN,
            anomaly_reasons JSONB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    cursor.execute(
        "ALTER TABLE predictions ADD COLUMN IF NOT EXISTS is_anomaly BOOLEAN;"
    )

    cursor.execute(
        "ALTER TABLE predictions ADD COLUMN IF NOT EXISTS anomaly_reasons JSONB;"
    )

    connection.commit()
    cursor.close()
    connection.close()


def save_prediction(
    sensor_data: dict,
    features: dict,
    prediction: dict,
    anomaly: dict
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO predictions (
            machine_id,
            temperature,
            vibration_total,
            rpm,
            risk_level,
            failure_probability,
            recommended_action,
            sensor_data,
            features,
            is_anomaly,
            anomaly_reasons
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """,
        (
            prediction["machine_id"],
            features["temperature"],
            features["vibration_total"],
            features["rpm"],
            prediction["risk_level"],
            prediction["failure_probability"],
            prediction["recommended_action"],
            Json(sensor_data),
            Json(features),
            anomaly["is_anomaly"],
            Json(anomaly["anomaly_reasons"])
        )
    )

    prediction_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return prediction_id


def get_recent_predictions(limit: int = 20):
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT
            id,
            machine_id,
            temperature,
            vibration_total,
            rpm,
            risk_level,
            failure_probability,
            recommended_action,
            is_anomaly,
            anomaly_reasons,
            created_at
        FROM predictions
        ORDER BY created_at DESC
        LIMIT %s;
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

