# Script to publish dummy sensor data on a public (!) MQTT server
# Created by M. Wiehl with ChatGPT on the 12.11.2024

# run script in seperate terminal window

import paho.mqtt.client as mqtt
import time
import json


import random

# MQTT Broker settings
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "mdne/dummy_sensor2"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(BROKER, PORT, 60)

# Publish dummy sensor data
def publish_dummy_data():
    while True:
        # Create a dummy sensor data payload
        sensor_data = {
            "temperature": round(random.uniform(20.0, 25.0), 2),
            "humidity": round(random.uniform(30.0, 50.0), 2),
            "pressure": round(random.uniform(1000, 1020), 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Convert data to JSON
        payload = json.dumps(sensor_data)
        

        # Save JSON data to a file
        file_path = "/Users/satya/Documents/Abhilasha/OTH_Sem3/Modern Databases & NoSQL (MDNE)/MDNE_Project/Files for the project/sensor_data.json"  # Specify the local file path

        with open(file_path, 'w') as file:
            file.write(payload)

        print(f"Data has been saved to {file_path}")
        # Publish the payload to the MQTT topic
        client.publish(TOPIC, payload)
        print(f"Published data: {payload}")

        # Wait before sending the next data packet
        time.sleep(2)

# Start transmitting dummy data
try:
    publish_dummy_data()
except KeyboardInterrupt:
    print("\nTransmission stopped by user.")
finally:
    client.disconnect()
