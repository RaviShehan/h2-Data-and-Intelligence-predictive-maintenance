import json
import random
import time
from datetime import datetime

from kafka import KafkaProducer


KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "machine.sensor.raw"


def generate_raw_sensor_data(machine_id: str) -> dict:
    return {
        "machine_id": machine_id,
        "temperature": round(random.uniform(35, 90), 2),
        "vibration_x": round(random.uniform(0.1, 2.8), 3),
        "vibration_y": round(random.uniform(0.1, 2.8), 3),
        "vibration_z": round(random.uniform(0.1, 2.8), 3),
        "rpm": random.randint(800, 6000),
        "timestamp": datetime.utcnow().isoformat()
    }


def apply_edge_filtering(sensor_data: dict) -> dict:
    filtered_data = sensor_data.copy()

    filtered_data["temperature"] = round(sensor_data["temperature"], 1)
    filtered_data["vibration_x"] = round(sensor_data["vibration_x"], 2)
    filtered_data["vibration_y"] = round(sensor_data["vibration_y"], 2)
    filtered_data["vibration_z"] = round(sensor_data["vibration_z"], 2)

    return filtered_data


def validate_telemetry(sensor_data: dict) -> bool:
    if sensor_data["machine_id"].strip() == "":
        return False

    if not 0 <= sensor_data["temperature"] <= 120:
        return False

    if not 0 <= sensor_data["vibration_x"] <= 5:
        return False

    if not 0 <= sensor_data["vibration_y"] <= 5:
        return False

    if not 0 <= sensor_data["vibration_z"] <= 5:
        return False

    if not 0 <= sensor_data["rpm"] <= 10000:
        return False

    return True


def create_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value).encode("utf-8")
    )


def run_edge_device():
    producer = create_kafka_producer()

    machine_ids = [
        "EDGE_MACHINE_01",
        "EDGE_MACHINE_02",
        "EDGE_MACHINE_03"
    ]

    print("H1 Edge Device Simulator started")
    print(f"Sending validated telemetry to Kafka topic: {KAFKA_TOPIC}")
    print()

    while True:
        machine_id = random.choice(machine_ids)

        raw_data = generate_raw_sensor_data(machine_id)
        filtered_data = apply_edge_filtering(raw_data)

        if validate_telemetry(filtered_data):
            producer.send(KAFKA_TOPIC, filtered_data)
            producer.flush()

            print("Sent filtered telemetry:")
            print(filtered_data)
            print()
        else:
            print("Invalid telemetry dropped:")
            print(filtered_data)
            print()

        time.sleep(3)


if __name__ == "__main__":
    run_edge_device()