import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_etc",
    use_pure = True
)


id= input("Enter id whose moisture_level to be updated : ")
moisture_level= input("Enter new moisture_level : ")

query = f"update soil_moisture1 SET moisture_level = '{moisture_level}' where id = '{id}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()