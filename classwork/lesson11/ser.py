import pickle

# print(dir(pickle))

obj = {
    "123": 123,
    "abc": "ABC"
}

def summ(a, b):
    return a + b

inp = input("1 - Новая сессия работы с программой \n2 - восстановить сессию") 
result = 0
if inp == "1":
    num1 = int(input("Число 1 "))
    num2 = int(input("Число 2 "))

    result = summ(num1, num2)
    fileResult = open("result.pkl", "wb")
    pickle.dump(result, fileResult, protocol=3)
    # fileResult.close()
else:
    fileLoad = open("result.pkl", "rb")
    result = pickle.load(fileLoad)

print(result)

# print(obj)
# print(type(obj))
# fd = open("pickle.pkl", "wb")
# print(fd)
# pickle.dump(obj, fd, protocol=3)
# rf = open("pickle.pkl", "rb")
# obj2 = pickle.load(rf, fix_imports=True, encoding="ASCII")
# print(obj2)
# dmp = pickle.dumps(obj)
# print(dmp)











# print(pickle.HIGHEST_PROTOCOL)

