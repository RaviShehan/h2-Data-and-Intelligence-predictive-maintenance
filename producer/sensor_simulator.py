import random
import time
import requests


API_URL = "http://127.0.0.1:8000/predict"


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


while True:
    sensor_data = generate_sensor_data()

    try:
        response = requests.post(API_URL, json=sensor_data)
        print("Input:", sensor_data)
        print("Prediction:", response.json()["prediction"])
        print("-" * 50)

    except Exception as error:
        print("Error sending data:", error)

    time.sleep(3)