import paho.mqtt.client as mqtt
import sqlite3

def update_status(appliance, status):
    conn = sqlite3.connect("home_automation.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appliance_status (appliance_name, status) VALUES (?, ?)",
        (appliance, status)
    )
    conn.commit()
    conn.close()

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    appliance, status = message.split(",")

    update_status(appliance, status)
    print(f"{appliance} turned {status}")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("home/control")

print("Device is ready to receive commands...")
client.loop_forever()