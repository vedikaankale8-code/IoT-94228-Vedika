import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    appliance = input("Enter appliance name (Light/Fan/AC): ")
    status = input("Enter status (ON/OFF): ")

    message = f"{appliance},{status}"
    client.publish("home/control", message)

    print(f"Command sent → {message}")