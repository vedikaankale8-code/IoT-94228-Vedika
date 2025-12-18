import mysql.connector

connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_etc",
    use_pure=True
)

query="select * from sensor_readings1";

cursor=connection.cursor()

cursor.execute(query)

sensor_readings1=cursor.fetchall()

for Sensor_readings1 in sensor_readings1:
    print(Sensor_readings1)
    
cursor.close()

connection.close()