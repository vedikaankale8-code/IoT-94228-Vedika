import mysql.connector

connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_etc",
    use_pure=True
)

query="select * from soil_moisture1";

cursor=connection.cursor()

cursor.execute(query)

soil_moisture1=cursor.fetchall()

for Soil_moisture1 in soil_moisture1:
    print(Soil_moisture1)
    
cursor.close()

connection.close()