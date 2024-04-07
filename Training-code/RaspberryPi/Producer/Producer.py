"""
Smart Sensor: Producer
This script is used for generating the sample data from the "test_cases.csv"
and publish them to the MQTT Broker
"""

# Importing relevant modules
import pandas as pd
import time
import paho.mqtt.client as mqtt
import json

# let's connect to the MQTT broker
MQTT_BROKER_URL    = "raspberrypi.local"
MQTT_PUBLISH_TOPIC = "@msg/data"

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL)

# Read data from "test_cases.csv"
df = pd.read_csv('test_cases.csv')

# Iterate over each row in the DataFrame
for index, row in df[0:400:20].iterrows():
    payload = row.to_dict()

    # publish the data to MQTT Broker
    mqttc.publish(MQTT_PUBLISH_TOPIC, json.dumps(payload))
    print(f"Published new measurement: {json.dumps(payload)}")

    # define data generating frequency
    time.sleep(5)