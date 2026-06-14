import json
import requests
from kafka import KafkaConsumer


KAFKA_TOPIC = "machine.sensor.raw"
KAFKA_SERVER = "localhost:9092"
API_URL = "http://127.0.0.1:8000/predict"


consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="h2-prediction-consumer",
    value_deserializer=lambda message: json.loads(message.decode("utf-8"))
)


print("Kafka prediction consumer started...")

for message in consumer:
    sensor_data = message.value

    try:
        response = requests.post(API_URL, json=sensor_data, timeout=5)
        prediction = response.json()["prediction"]

        print("Received from Kafka:", sensor_data)
        print("Prediction:", prediction)
        print("-" * 60)

    except Exception as error:
        print("Error calling prediction API:", error)