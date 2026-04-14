import random

S = 1

L = [
    lambda : random.random(),
    lambda : random.random(),
    lambda : random.random()
]

# def three_item_random_arr():
#     return [
#     random.random(),
#     random.random(),
#     random.random()
# ]


# print(three_item_random_arr())
# print(three_item_random_arr())
# print(three_item_random_arr())

for l in L:
    print(l())
    print(l())
    print(l())

Dict = {
    1 : (lambda: print('Monday')),
    2 : (lambda: print('Tuesday')),
    3 : (lambda: print('Wednesday')), 
    4 : (lambda: print('Thursday')), 
    5 : (lambda: print('Friday')),
    6 : (lambda: print('Saturday')), 
    7 : (lambda: print('Sunday'))
}

tsd = Dict[2]
tsd()

numbers=[0,1,2,3,4,5,6,7,8,9,10] 
print(list(
    filter(lambda x:x%3==0, numbers)
    ))


print(range(11))
print(type(range(11)))

# for i in range(11):
#     print(i)

even = lambda x: x%2 == 0 and x != 0 
print(list(filter(even, range(11))))


arr = ['cat', 'dog', 'cow']

l1 = []
for i in arr:
    l1.append(i.capitalize())

l2 = list(map(lambda x: x.capitalize(), arr))

print(l2, l1)

from functools import reduce
numbers=[0,1,2,3,4,5,6,7,8,9,10]


print(reduce(lambda x,y: y - x, numbers))

print((lambda x: x if x + 2 else x - 2)(True))