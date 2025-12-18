from flask import Flask, request

app = Flask(__name__)

@app.route('/send', methods=['GET'])
def receive():
    temp = request.args.get('temp')
    light = request.args.get('light')

    if temp:
        open("temperature.txt", "a").write(temp + "\n")
    if light:
        open("light.txt", "a").write(light + "\n")

    return "Data Stored Successfully"

@app.route('/temperature')
def show_temp():
    return "<pre>" + open("temperature.txt").read() + "</pre>"

@app.route('/light')
def show_light():
    return "<pre>" + open("light.txt").read() + "</pre>"

app.run()
