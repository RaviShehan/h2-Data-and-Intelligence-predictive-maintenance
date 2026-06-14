import json
import random
import time
from kafka import KafkaProducer


KAFKA_TOPIC = "machine.sensor.raw"
KAFKA_SERVER = "localhost:9092"


producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda data: json.dumps(data).encode("utf-8")
)


def generate_sensor_data():
    condition = random.choice(["NORMAL", "WARNING", "CRITICAL"])

    if condition == "NORMAL":
        temperature = random.uniform(35, 49)
        vibration_x = random.uniform(0.1, 0.4)
        vibration_y = random.uniform(0.1, 0.4)
        vibration_z = random.uniform(0.1, 0.4)

    elif condition == "WARNING":
        temperature = random.uniform(50, 69)
        vibration_x = random.uniform(0.4, 0.8)
        vibration_y = random.uniform(0.4, 0.8)
        vibration_z = random.uniform(0.4, 0.8)

    else:
        temperature = random.uniform(70, 90)
        vibration_x = random.uniform(1.0, 1.5)
        vibration_y = random.uniform(1.0, 1.5)
        vibration_z = random.uniform(1.0, 1.5)

    return {
        "machine_id": "MACHINE_01",
        "temperature": round(temperature, 2),
        "vibration_x": round(vibration_x, 2),
        "vibration_y": round(vibration_y, 2),
        "vibration_z": round(vibration_z, 2),
        "rpm": 1450
    }


print("Kafka sensor producer started...")

while True:
    sensor_data = generate_sensor_data()
    producer.send(KAFKA_TOPIC, value=sensor_data)
    producer.flush()

    print("Sent to Kafka:", sensor_data)
    time.sleep(3)