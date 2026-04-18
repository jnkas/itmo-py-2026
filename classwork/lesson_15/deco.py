arr = []

def f1 (i):
    i += 1
    return i

def f4 (i):
    i += 4
    return i

def f10 (i):
    i += 10
    return i

arr.append(f1)
arr.append(f4)
arr.append(f10)
print(arr)

for fn in arr:
    print(fn(10))


def render(text):
    # print("Начало"), а где конец?
    return f"Это функция render выводит {text.capitalize()}"

print(
    render("москва"),
    render("саратов"),
)

# Вызов декоратора можно переписать так:
def decorator_render(func):
    def wrapper(text):
        #что -то до
        res = func(text)
        #что -то после
        return res
    return wrapper

# render1 = decorator_render(render)

# print(render1("москва"))

@decorator_render
def render(text):
    return f"Это функция render выводит {text.upper()}"

print(render("лондон"))



