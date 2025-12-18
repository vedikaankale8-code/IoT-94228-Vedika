import mysql.connector
from datetime import datetime

connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_etc",
    use_pure=True
)

current_datetime=datetime.now()
sensor_id=int(input("Enter sensor_id:"))
moisture_leve=input("Enter moisture_level:")
current_time=input("Enter current_time:")

query=f"insert into soil_moisture1 values({sensor_id},'{moisture_leve}','{current_time}')";

cursor=connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()
