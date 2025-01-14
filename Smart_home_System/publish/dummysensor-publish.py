import time
import random
import json
import redis
import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet

# MQTT Configuration
BROKER = "mqtt-broker"
PORT = 1883
TOPIC_PREFIX = "sensor"  # Topic prefix for sensors
SENSOR_IDS = range(1, 43)  # SensorIDs from 1 to 42

# Redis Configuration
REDIS_HOST = "redis"
REDIS_PORT = 6379

# Load encryption key
with open("encryption_key_user1.key", "rb") as key_file:
    key = key_file.read()
cipher = Fernet(key)

# Connect to Redis
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# Sensor type IDs
SENSOR_TYPE_IDS = {
    "temperature": 101,
    "humidity": 102,
    "pressure": 103,
    "light": 104,
    "sound": 105,
    "vibration": 106,
}

# Publish dummy sensor data for all sensors
def publish_dummy_data():
    while True:
        for sensor_id in SENSOR_IDS:
            # Create dummy sensor data with multiple types
            sensor_data = {
                "sensor_id": sensor_id,
                "temperature": {
                    "value": round(random.uniform(20.0, 25.0), 2),
                    "type_id": SENSOR_TYPE_IDS["temperature"]
                },
                "humidity": {
                    "value": round(random.uniform(30.0, 50.0), 2),
                    "type_id": SENSOR_TYPE_IDS["humidity"]
                },
                "pressure": {
                    "value": round(random.uniform(1000, 1020), 2),
                    "type_id": SENSOR_TYPE_IDS["pressure"]
                },
                "light": {
                    "value": round(random.uniform(300, 800), 2),
                    "type_id": SENSOR_TYPE_IDS["light"]
                },
                "sound": {
                    "value": round(random.uniform(40, 80), 2),
                    "type_id": SENSOR_TYPE_IDS["sound"]
                },
                "vibration": {
                    "value": round(random.uniform(0.01, 0.10), 2),
                    "type_id": SENSOR_TYPE_IDS["vibration"]
                },
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            # Serialize and encrypt the data
            json_data = json.dumps(sensor_data)
            encrypted_message = cipher.encrypt(json_data.encode())

            # Save encrypted data to Redis
            redis_key = f"sensor{sensor_id}:latest_sensor_data"
            redis_client.set(redis_key, encrypted_message.decode())

            # Publish encrypted payload to MQTT
            topic = f"{TOPIC_PREFIX}{sensor_id}/data"
            client.publish(topic, encrypted_message)
            print(f"Published encrypted data to topic {topic}: {encrypted_message.decode()}")

        # Delay to simulate real-time data
        time.sleep(5)

# Initialize MQTT client
client = mqtt.Client()
client.on_connect = lambda client, userdata, flags, rc: print("Connected to MQTT broker" if rc == 0 else f"Failed to connect, return code {rc}")

# Connect to MQTT broker and start publishing
try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    publish_dummy_data()
except Exception as e:
    print(f"Failed to connect or publish: {e}")
finally:
    client.loop_stop()
    client.disconnect()
