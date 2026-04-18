# =========================================
# 🌐 ЗАДАЧА 2: Ограничение частоты API (rate limit)
# =========================================

# todo Нужно создать декоратор, который разрешает не более 3 
# вызовов функции за 5 секунд, а если лимит превышен
# возвращает сообщение "Слишком много запросов"
# Применить к функции получения данных.


import time

def rate_limit(max_calls, period):
    calls = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            current = time.time()

            # удаляем старые вызовы
            while calls and current - calls[0] > period:
                calls.pop(0)

            if len(calls) >= max_calls:
                return "Слишком много запросов"

            calls.append(current)
            return func(*args, **kwargs)

        return wrapper
    return decorator


@rate_limit(3, 5)
def get_data():
    return "Данные получены"


print(get_data())
print(get_data())
print(get_data())
print(get_data())  # здесь сработает ограничение