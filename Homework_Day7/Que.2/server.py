from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/soil_moisture1')
def create_soil_moistures1():
   
    sensor_id= request.form.get('sensor_id')
    moisture_level= request.form.get('moisture_level')
    datetime= request.form.get('datetime')

    query = f"insert into soil_moisture1 values({sensor_id}, {moisture_level},'{datetime}');"

    executeQuery(query=query)

    return "sensor moisture reading is added successfully"

@server.get('/soil_moisture1')
def retrieve_soil_moistures1():
    
    query = "select * from soil_moisture1;"
    
    data = executeSelectQuery(query=query)

    return f"soil_moisture1 : {data}"

@server.put('/soil_moisture1')
def update_soil_moistures1():

    sensor_id = request.form.get('sensor_id')
    moisture_level= request.form.get('moisture_level')

    query = f"update sensor_moisture1 SET moisture_level = '{moisture_level}' where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "soil_moisture1 is updated successfully"

@server.delete('/soil_moisture1')
def delete_soil_moistures1():
    
    sensor_id = request.form.get('sensor_id')

    query = f"delete from soil_moisture1 where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "soil_moisture1 is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)