#todo: Создайте объект сериализации любым методом для соседа, 
# запишите его в файл,
# передайте его ему для считывания. 
# Соседу необходимо десириализовать полученый объект.


#todo: Заданы два списка. Необходимо их сериализовать в один файл.

import pickle

ch = input("1. сериализуем \n2. Десериализуем")
if ch == "1":
    list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
    list_two = [False, 'Sparse is better than dense.', {'age': 90}]

    obj = {
        "list_one": list_one,
        "list_two": list_two
    }

    print(obj)

    file = open("obj.pkl", "wb")
    pickle.dump(obj, file, protocol=3)
    file.close()

elif ch == "2":
    name = input("Название файла: ")
    file = open(name, "rb")
    file.close()
    data = pickle.load(file)
    print(data["list_one"][0])
    print(data["list_two"])
