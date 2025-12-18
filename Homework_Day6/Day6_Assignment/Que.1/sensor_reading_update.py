import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_etc",
    use_pure = True
)


id= input("Enter id whose temperature to be updated : ")
temperature= input("Enter new temperature : ")

query = f"update sensor_readings1 SET temperature = '{temperature}' where id = '{id}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()