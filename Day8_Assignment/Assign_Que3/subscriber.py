import paho.mqtt.client as mqtt
import sqlite3

def save_data(parameter, value):
    conn = sqlite3.connect("healthcare.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO patient_health (parameter, value) VALUES (?, ?)",
        (parameter, value)
    )
    conn.commit()
    conn.close()

def send_alert(message):
    print("ALERT TO DOCTOR:", message)

def on_message(client, userdata, msg):
    value = int(msg.payload.decode())

    if msg.topic == "patient/pulse":
        save_data("Pulse", value)
        if value < 60 or value > 100:
            send_alert(f"Abnormal Pulse Detected: {value}")

    elif msg.topic == "patient/spo2":
        save_data("SpO2", value)
        if value < 95:
            send_alert(f"Low SpO2 Level Detected: {value}%")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("patient/pulse")
client.subscribe("patient/spo2")

print("Doctor monitoring system started...")
client.loop_forever()