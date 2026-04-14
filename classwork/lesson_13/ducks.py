"""
Задача: Аналитика убывания перелётных птиц заграницу

Eсть датасет наблюдений за птицами за 31 день.
Нужно с помощью генераторов:
    1. Заполнить пропущенные дни (с 1 по 31), иначе график будет некорректным
    2. Получить список количества всех птиц по дням (для графика)
    3. Получить данные только по "уткам" за последние 7 дней
    4. Построить 2 графика:
        - общее количество птиц по дням
        - утки за последнюю неделю

Исходные данные:
"""
# data = {
#     1: [{"утка": 5}, {"лебедь": 5}], 
#     2: [("утка", 5), ("лебедь", 5)], 
#     ...
#     30: ...
# }
data = {
    1: [("утка", 5), ("лебедь", 3)],
    2: [("журавль", 2)],
    4: [("гусь", 1)],
    7: [("журавль", 8), ("орёл", 1)],
    10: [("голубь", 6)],
    15: [("утка", 10)],
    18: [("ласточка", 1)],
    22: [("журавль", 4)],
    25: [("голубь", 7)],
    30: [("утка", 6)]
}

print(data.get(3, []))
filled_data = {day: data.get(day, []) for day in range(1, 32)}
print(filled_data)
import matplotlib.pyplot as plt



total_birds_per_day = [

]

# for day in filled_data:
#     item_as_list_of_bird = filled_data[day]
#     # print(filled_data[item])
#     count_per_day = 0
#     for birds in item_as_list_of_bird:
#         # for item in birds:
#         count_per_day += birds[1]
#         # print(birds)

#     print(count_per_day)
#     total_birds_per_day.append(count_per_day)

total_birds_per_day = [
    sum(count for bird, count in filled_data[day]) 
    for day in filled_data
]

total_birds_per_day2 = [
    sum(count for bird, count in data[day]) 
    for day in data
]

total_ducks_per_last_week = [
    sum(count for bird, count in filled_data[day] if bird == "утка") 
    for day in range(24, 32)
]

print(total_ducks_per_last_week)



plt.figure()
plt.plot(range(1, 32), total_birds_per_day)
plt.title("Количество птиц по дням")
plt.xlabel("Дни")
plt.ylabel("количество птиц")
plt.grid()

plt.figure()
plt.plot(range(24,32), total_ducks_per_last_week)
plt.title("Количество уток за последнюю неделю")
plt.xlabel("Дни")
plt.ylabel("количество")
plt.grid()

plt.show()




