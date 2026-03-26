# Задача 1 - Подсчет повторений
# Дан список: numbers = [1, 2, 2, 3, 3, 3]
# Создать словарь:
# 1 = 1
# 2 = 2
# 3 = 3
# Print(число → сколько раз встречается)

dict = {}
numbers = [1, 2, 2, 3, 3, 3, 3]

for i in numbers:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
    

print(dict)