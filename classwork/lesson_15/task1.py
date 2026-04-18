# todo: Реализовать декоратор который подсчитывает время выполнения функции.
# Для этого необходимо взять время до начала запуска функции и после ее окончания.
# Проверить декоратор для различного рода алгоритмов сортировок на большом наборе данных.


import time
import random

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start:.6f} сек")
        return result
    return wrapper


@timer
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


@timer
def python_sort(arr):
    return sorted(arr)


data = [random.randint(0, 10000) for _ in range(1000)]

bubble_sort(data)
python_sort(data)