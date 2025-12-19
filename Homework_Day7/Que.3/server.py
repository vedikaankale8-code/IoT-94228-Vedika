from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/home_monitoring1')
def create_home_monitoring1():
   
    id= request.form.get('id')
    light_status= request.form.get('light_status')
    fan_status= request.form.get('fan_status')
    temperature= request.form.get('temperature')

    query = f"insert into home_monitoring1 values({id}, '{light_status}','{fan_status}','{temperature}');"

    executeQuery(query=query)

    return "home monitoring reading is added successfully"

@server.get('/home_monitoring1')
def retrieve_home_monitoring1():
    
    query = "select * from home_monitoring1;"
    
    data = executeSelectQuery(query=query)

    return f"home_monitoring1 : {data}"

@server.put('/home_monitoring1')
def update_home_monitoring1():

    id = request.form.get('id')
    temperature= request.form.get('temperature')

    query = f"update home_monitoring1 SET temperature = '{temperature}' where id = '{id}';"

    executeQuery(query=query)

    return "home_monitoring1 is updated successfully"

@server.delete('/home_monitoring1')
def delete_home_monitoring1():
    
    id = request.form.get('id')

    query = f"delete from home_monitoring1 where id = '{id}';"

    executeQuery(query=query)

    return "home_monitoring1 is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)