# Script to receive data and store only current values in variables
# Created by M. Wiehl with ChatGPT on the 12.11.2024

# run file in seperat terminal window

import paho.mqtt.client as mqtt
import json

# MQTT Broker settings
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "mdne/dummy_sensor_data2"

# Variables to store the latest sensor data
latest_temperature = None
latest_humidity = None
latest_pressure = None
latest_timestamp = None

# Callback function when a message is received
def on_message(client, userdata, message):
    global latest_temperature, latest_humidity, latest_pressure, latest_timestamp
    
    # Decode the received message
    payload = message.payload.decode()
    print(f"Received message: {payload}")
    
    # Parse the JSON payload
    try:
        sensor_data = json.loads(payload)
        
        # Update the variables with the latest data
        latest_temperature = sensor_data.get("temperature")
        latest_humidity = sensor_data.get("humidity")
        latest_pressure = sensor_data.get("pressure")
        latest_timestamp = sensor_data.get("timestamp")

        # Print the updated variables
        print("Updated Sensor Data:")
        print(f"Temperature: {latest_temperature} °C")
        print(f"Humidity: {latest_humidity} %")
        print(f"Pressure: {latest_pressure} hPa")
        print(f"Timestamp: {latest_timestamp}")

    except json.JSONDecodeError:
        print("Failed to decode JSON payload")

# Create an MQTT client and configure callbacks
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker and subscribe to the topic
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

# Start the MQTT client loop to process network traffic and dispatch callbacks
print("Listening for sensor data...")
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscription stopped by user.")
finally:
    client.disconnect()
