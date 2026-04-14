# Угадай число, надо загадть число от 1 до 100. Пользователь вводит число, пока не угадает, 5 попыток.

import random
import json
rn = random.randint(1, 100)
counter = 5

programData = {
    "rn": random.randint(1, 100),
    "counter": counter
}

# rn, counter

for i in range(counter, 0, -1):
    print(f"Осталось попыток: {i}")
    print(f"Для перехода в меню, нажмите \"М\"")

    inp = input("Введите число: ")

    # global rn

    if inp == "M":
        print("1. Продолжить")
        print("2. Сохранить")
        print("3. Загрузить")
        print("0. Выход")

        inp = input("Выберите из меню: ")


        if inp == "2":
            # Сохраняем
            name = input("Название сейва")
            file = open("save.json", "wt")
            json.dump({
                "num": rn,
                "attempts": counter
            }, file)
            file.close()

        if inp == "3":
            file = open("save.json", "rt")
            data = json.load(file)
            
            programData["rn"] = data["num"]
            programData["counter"] = data["attempts"]


    
        
    num = int(inp)
    
    if num == rn:
        print(f"Поздравляю! Вы угадали число {rn}")
        break
    elif num < rn:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
else:
    print(f"Вы проиграли. Загаданное число было {rn}")