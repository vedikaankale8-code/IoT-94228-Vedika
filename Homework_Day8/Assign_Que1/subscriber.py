import paho.mqtt.client as mqtt
import sqlite3

def insert_data(sensor, value):
    conn = sqlite3.connect("smart_home.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sensor_data (sensor_type, value) VALUES (?, ?)",
        (sensor, value)
    )
    conn.commit()
    conn.close()

def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    
    if msg.topic == "sensor/ldr":
        insert_data("LDR", value)
        print(f"LDR data saved: {value}")
    
    elif msg.topic == "sensor/lm35":
        insert_data("LM35", value)
        print(f"Temperature data saved: {value}")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe("sensor/ldr")
client.subscribe("sensor/lm35")

print("Subscriber started...")
client.loop_forever()
