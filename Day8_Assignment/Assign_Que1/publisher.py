import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"
client = mqtt.Client()

client.connect(broker, 1883, 60)

while True:
    ldr_value = random.randint(0, 1023)      # Light intensity
    temp_value = round(random.uniform(20, 35), 2)  # Temperature

    client.publish("sensor/ldr", ldr_value)
    client.publish("sensor/lm35", temp_value)

    print(f"Published LDR: {ldr_value}, Temperature: {temp_value}")

    time.sleep(5)
