students = [
    {
        "name": "Василий",
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
        "age": 29,
        "homework": {
            "task1": True,
            "task2": True,
            "task3": True
        },
        "all_homeworks": 3
    }
]

def save_to_text (students):
    file = open("students.txt", "w", encoding="utf-8")
    file.write(str(students))
    file.close()


save_to_text(students)

import json

def save_to_json(students):
    file = open("students.json", "w", encoding="utf-8")
    json.dump(students, file, indent=4, ensure_ascii=False)
    file.close()

# save_to_json(students)

def read_from_json():
    file = open("students.json", "r", encoding="utf-8")
    data = file.read()
    # print(type(data))
    data = json.load(file)
    
    global students
    students = data
    file.close()

read_from_json()



print(students)