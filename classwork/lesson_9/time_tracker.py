# Посчитать сколько часов отработал сотрудник и сколько недоработал. 
# Рабочий день 8 часов.
#
# Пример:
# Отработано: 7 часов 30 минут
# Перерыв: 30 минут
# Недоработка: 1 час

from datetime import datetime

start = input("Начало (HH:MM): ")
end = input("Конец (HH:MM): ")
break_time = int(input("Перерыв (мин): "))

start_time = datetime.strptime(start, "%H:%M")
print(start_time)
end_time = datetime.strptime(end, "%H:%M")

delta = end_time - start_time

total_minutes = int(delta.total_seconds() / 60)
work_minutes = total_minutes - break_time

hours = work_minutes // 60
minutes = work_minutes % 60

print(f"Отработано: {hours} часов {minutes} минут")
print(f"Перерыв: {break_time} минут")

if work_minutes > 480:
    print("Переработка:", (work_minutes - 480) // 60, "часов")
elif work_minutes < 480:
    print("Недоработка:", (480 - work_minutes) // 60, "часов")
else:
    print("Норма выполнена")