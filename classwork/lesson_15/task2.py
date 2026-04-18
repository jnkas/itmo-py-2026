"""
ЗАДАЧА 1: Логирование заказов (бизнес)
Условие:
Ты разрабатываешь систему интернет-магазина.
Нужно создать декоратор, который будет логировать:
- имя функции
- аргументы
- результат работы

Применить его к функции обработки заказа.
"""

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        print("-" * 30)
        return result
    return wrapper


@log
def process_order(price, quantity):
    return price * quantity


process_order(100, 3)
process_order(250, 2)