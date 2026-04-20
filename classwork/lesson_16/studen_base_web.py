from flask import Flask

students = [
    {
        "name": "Василий",
        "id": 1,
        "age": 20,
        "homework": {
            "task1": True,
            "task2": True,
            "task3": False
        },
        "all_homeworks": 3
    },
    {
        "name": "Маша",
        "id": 2,
        "age": 29,
        "homework": {
            "task1": True,
            "task2": True,
            "task3": True
        },
        "all_homeworks": 3
    }
]

app = Flask(__name__)

@app.get("/api/students")
def show_all():

    html = ""
    html += '<h1>Список студентов курса:</h1>'

    for student in students:
        # print(student)
        html += f"<p><a href='/api/student/{student["id"]}'>"
        html += f"\nИмя: {student["name"]} "
        html += f"Возраст: {student["age"]}"
        # html += "Домашние задания: "
        html += "</p></a>"
        # print(student["homework"])
        dz = student["homework"]
        for task in dz:
            print(f"{task} : {dz[task]}") 

    return html

@app.get("/api/student/<int:id>")
def show_student_details(id):
    html = '''
    <style>
        h1 + p {
            background: #d6ffe7;
            padding: 15px;
            border-radius: 50px;
            text-align: center;
        }
    </style>
    '''
    html += "<h1> Домашние задания студента</h1>"
    dz = ""
    for student in students:
        if id == student["id"]: 
            dz = student["homework"]

            html += f"<p> {student["name"]}<p>"

    for task in dz:
        html += f"{task} : {dz[task]}"

    return html

    

# show_all()
app.run(port=5001)