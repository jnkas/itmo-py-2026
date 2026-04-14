print(
    lambda smthing: smthing + " что-то"
    )

def function1 (smthing):
    return smthing + " что-то"


fn1 = function1
print(fn1)
print(type(fn1))

print(fn1("111"))

num = 1 

num_plus_2_and_minus_num = lambda num1, num2: num1 + 2 - num2

second_fn = lambda *args: args

print(
    num_plus_2_and_minus_num(1, 2),
    num_plus_2_and_minus_num(999, 2),
    num_plus_2_and_minus_num(888, 66),
    second_fn(1, 2, 4)
)

inp1 = input("введите ваше имя: ")
inp2 = input("введите вашу фамилию: ")

users = [{
    "name": "Иван",
    "surname": "Иванов"
}]

util_fi_combine = lambda s1, s2: {"name": s1, "surname": s2}

users.append(util_fi_combine(inp1, inp2))

print(users)




