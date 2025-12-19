from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/sensor_readings1')
def create_sensor_readings1():
   
    id = request.form.get('id')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')
    timestamp = request.form.get('timestamp')

    query = f"insert into sensor_readings1 values({id}, {temperature}, {humidity},'{timestamp}');"

    executeQuery(query=query)

    return "sensor reading is added successfully"

@server.get('/sensor_readings1')
def retrieve_sensor_readings1():
    
    query = "select * from sensor_readings1;"
    
    data = executeSelectQuery(query=query)

    return f"sensor_readings1 : {data}"

@server.put('/sensor_readings1')
def update_sensor_readings1():

    id = request.form.get('id')
    temperature = request.form.get('temperature')

    query = f"update sensor_readings1 SET temperature = '{temperature}' where id = '{id}';"

    executeQuery(query=query)

    return "temperature is updated successfully"

@server.delete('/sensor_readings1')
def delete_sensor_readings1():
    
    humidity = request.form.get('humidity')

    query = f"delete from sensor_readings1 where humidity = '{humidity}';"

    executeQuery(query=query)

    return "sensor_readings1 is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)