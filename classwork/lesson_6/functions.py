name = ""
name = "H"


def nameFunc():
    x = 1 + 1
    print("шаг 1")

    return (1, 5)

print(nameFunc())
# (nameFunc())
# result = 0

# def summ(a, b=0):
#     result = a + b
#     print(result)
#     return result

def parser(name, age, position, salary, e, f):

    print(name, age, position, salary, e, f)
    # result = list(name, age, position, salary, e, f)
    # return result

parser(position="director", name="Ivan", age=44, salary=100, e=0, f=0)
# print(p1)

# x1 = summ(6)
# x2 = summ(7, 3)
# x3 = summ(99, 8)

# print(result, x1)

def raznost(a, b, *args):
    print("---", len(args))
    result = a - b
    result = (result, ) + args

    return result

print(raznost(5, 7, 8, 9, 10, 1111))
(-2, 8, 9, 10, 1111)

def multiple(**kwargs):
    print(kwargs)
    a = kwargs['first']
    b = kwargs['second']
    result = a * b
    return result

print(multiple(first=1, second=4, third=4 ))



result = 0

def summ(a, b=0):
    # scope - область видимости [result, a, b]
    global result
    print("-----", result)
    result = a + b
    print(result)
    return result

print(summ(1, 2))

# print(result, a, b)

def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num
    
    return incrementer


timer1 = counter()
timer2 = counter()

# print(counter())
print(timer1())
print(timer1())
print(timer1())
print(timer1())
print(timer1())
print(timer2())
print(timer2())


# print(counter)

