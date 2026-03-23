
print(type("1" + "1"), 1 + 1)

number = [1, 2]

list1 = [ 
    2, 
    3, 
    5, 
    True, 
    5,
    number, 
    [2, 5] 
]

[
    [0, 0, 0],
    [0, 1, 0]
]
list2 = list([1, "5"])
list3 = list("Привет!")

list4 = list2
list2[0] = 777
list4[0] = 888



print(list4, list2)


print(list2)
list2[1] = 77
print(list2)

num = 13
num2 = num
num += 1



print(num2)


print(list1)
print(list2)
print(list3)

hello = list3[:]
hello[2] = "1"

hello2 = list(hello)
print(hello2)

l1 = [1, 2]
l2 = [3, 4]

l3 = l1 + l2
print(l3)

print(2 not in [1, 2])
print(len(hello2))

arr = ["монеты", 6]
arr.append("книги")
arr.append(l2)
arr.clear()

arr = l3.copy()

print(arr.count(4))

arr.insert(0, 6)
arr.pop(2)
arr.append("кот")
print(arr)
arr.remove('кот')
arr.reverse()
arr.sort()

listNew = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

# inp = input("Строка")
# print(inp == inp[::-1])

print("Что-нибудь"[::-1])


print(arr.index(3))

input_list = [10, "S", 15, "A", 1]
for item in input_list:
    print(item)

print(list(range(5)))

counter = 0
for i in list(range(5)):
    counter += 1

print(counter)

for x in "3r":
 print('result', x )

for i in "Hello world":
#    print(i)
    
    if i == "o":
    #    break
       continue
    print(i)

for i in "Hello world":
   pass

while True:
   print("!")



     
    