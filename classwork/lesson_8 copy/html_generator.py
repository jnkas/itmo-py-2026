student = {
        "name": "Василий",
        "age": 20,
        "homework": {
            "task1": True,
            "task2": True,
            "task3": False
        },
        "all_homeworks": 3
    }

def create_html_page(student):
    file = open("index.html", "w", encoding="utf-8")

    student_info = ""

    student_info += "<h1>" + student["name"] + "</h1>\n"
    student_info += "<p> Возраст: " + str(student["age"]) + "</p>\n"


    task_info = ""

    dz = student["homework"]

    for task in dz:
        print(dz[task])

        flag = "Сделано" if dz[task] == True else "Не сделано"
        task_info += f"<li>{task} : {flag}</li>\n"


    html = f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Заголовок страницы, произвольный текст</title>    
        </head>
        <body>
            <a href="ya.ru"> текст </a>
            <!--h1>{student["name"]}</h1-->
            <!--p>Возраст: {student["age"]}</p-->

            {student_info}
            
            <h2>Домашние задания:</h2>
            <ol>
                {task_info}
            <ol>
        </body>
    </html>

    """

    file.write(html)
    file.close()

create_html_page(student)