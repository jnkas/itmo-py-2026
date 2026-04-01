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

# print(type(students))
# print(type(students[0]))
# print(type(students[0]["homework"]))

def show_menu():
    print("""
        1 - Создать карточку
        2 - Показать все
        3 - Найти по имени
        4 - Найти по сделанному заданию
        5 - Сохранить на диск(в файл)
        0 - Выход
          """)
    
def show_all():
    print('Список студентов курса:')

    for student in students:
        # print(student)
        print(f"\nИмя: {student["name"]}")
        print(f"Возраст: {student["age"]}")
        print("Домашние задания: ")
        # print(student["homework"])
        dz = student["homework"]
        for task in dz:
            print(f"{task} : {dz[task]}") 
            


def find_by_name():
    inp = input("Введите имя для поиска:")

    for student in students:
        name = student["name"]
        # print('-----', name)
        # print(inp.strip())
        # print(type(inp.strip().lower()))
        if name.strip().lower() == inp.strip().lower():
            #распечатать карточку нужного студента
            print(f"Студент с иенем {name} найден")
            return
        
    print("Студент не найден")

def find_by_done_task():
    inp = input("Введите номер дз для поиска:")
    keyName = "task" + inp

    for student in students:
        hw = student["homework"]

        taskValue = hw[keyName]
        if taskValue == True:
            #Печатаем студента
            print(f"\nИмя: {student["name"]}")

def create():

    inpName = input("Введите имя:")
    inpAge = input("Введите возраст:")

    homework = {}
    inpAll_homeworks = int(input("Введите количество заданий:"))
    print(range(1, 3 + 1))
    for item in range(1, inpAll_homeworks + 1):
        done = input(f"Задание {item} - выполнено? (y/n)")
        keyTask = 'task'+ str(item)
        homework[keyTask] = True if done == "y" else False

    student = {
        "name": inpName,
        "age": inpAge,
        "homework": homework,
        "all_homeworks": inpAll_homeworks
    }

    print(student)
    students.append(student)
    print("Студент " + student["name"] + " добавлен")


    # {
    #     "name": "Василий",
    #     "age": 20,
    #     "homework": {
    #         "task1": True,
    #         "task2": True,
    #         "task3": False
    #     },
    #     "all_homeworks": 3
    # }

def save():
    file = open("students.txt", "w", encoding='utf-8')

    for student in students:
        file.write(f"Имя: {student['name']}\n")
        file.write(f"Возраст: {student['age']}\n")
        
        dz = student["homework"]
        for task in dz:
            file.write(f"{task}: {dz[task]}\n")

        file.write("\n")

    
    file.close()
    print("Данные сохранены")

    

def processing(choice):
    
    match choice:
        case 1:
            create()
        case 2:
            #Показать все
            show_all()
        case 3:
            find_by_name()
        case 4:
            find_by_done_task()
        case 5:
            save()

def main():

    #читаем students.txt сохраняем в students
    
    while True:
        # Показываем меню
        show_menu()
        choice = int(input("Выберите пункт меню:"))
        
        #Обработка выбора
        processing(choice)

        if choice == 0:
            break



main()

