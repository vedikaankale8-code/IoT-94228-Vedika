# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/soil_moisture1', methods=['POST'])
def create_soil_moisture1():
    sensor_id= request.get_json().get('sensor_id')
    moisture_level= request.get_json().get('moisture_level')
    date_time= request.get_json().get('date_time')
    
    
    query = f"insert into soil_moisture1 values({sensor_id},{moisture_level},'{date_time}');"

    executeQuery(query=query)

    return "soil_moisture readings is added successfully"

@server.route('/soil_moisture1', methods=['GET'])
def retrieve_soil_moisture1():
    # create a select query
    query = "select * from soil_moisture1;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"soil_moisture1 : {data}"

@server.route('/soil_moisture1', methods=['PUT'])
def update_soil_moisture1():
    # extract data form form
    sensor_id= request.get_json().get('sensor_id')
    moisture_level= request.get_json().get('moisture_level')

    # create a query
    query = f"update soil_moisture1 SET moisture_level = '{moisture_level}' where sensor_id = '{sensor_id}';"

    # execute the query
    executeQuery(query=query)

    return "moisture_level is updated successfully"

@server.route('/soil_moisture1', methods=['DELETE'])
def delete_soil_moisture1():
    # extract data form form
    sensor_id= request.get_json().get('sensor_id')

    # create a query
    query = f"delete from soil_moisture1 where sensor_id= '{sensor_id}';"

    # execute the query
    executeQuery(query=query)

    return "sensor_id is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)