from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.get("/")
def get_html_page():
    return "Hello!"

@app.get("/students")
def get_students_data():

    obj = {
            "name": "Иван",
            "age": 20
        }

    return jsonify(obj)

@app.get("/getdata")
def get_data_from_anoter_server():
    print("мы получили запрос от браузера")

    res = requests.get("https://api.restful-api.dev/objects")
    data = res.json()
    print(data)

    return data[0]

@app.route("/getdata/<int:id>")
def get_data_by_id(id):

    print("мы получили запрос от браузера")

    return f"ваш запрошенный id {id}"

app.run(port=5000)