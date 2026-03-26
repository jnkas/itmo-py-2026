

person = {
    "name" : "Евгений",
    "age" : 100,
    20 : "Двадцать",
    1 : "Манго",
    2.7: 10,
    True: 'mango'
}

dict_sample = { 
    None: 'mango', 
    None: 'coco'
}

# kitchen = {}
# print(type(kitchen))

# kitchen = dict(frige="LG", microvawe="Samsung")

kitchen = {
    "frige":"LG", 
    "microvawe":"Samsung",
    10: 'ten'
}

# kitchen = {}

# frige = 'frige'

kitchen["frige"] = "Hunday"

kitchen_copy = kitchen
kitchen_copy["microvawe"] = "LG"

# del kitchen['frige']

# print('frige' in kitchen)
print(kitchen)
# print(type(sorted(kitchen)))
# print(kitchen_copy)

# print(type([{"frige": "LG"}, {10 : "ten"}][0]))

for k, v in kitchen.items():
    print(f"Ключ: {k}, Значение: {v}")

# kitchen.clear()
kitchen.get("frige2", "арбуз")

 
print(kitchen.items())

list1 = [1, 3, 5]
dict2 = dict.fromkeys(list1)
print(dict2)

item = dict2.pop(3)

print(dict2, item)

# print(type(person))
# print(person)
# print(dict_sample)

m = set([1, 2, 2, 3, 3, 3, 3])

m.add(4)
m.add(4)

cort = (
        ("2", "5"),
        ("2", "5"),
        ("2", "5"), 
        "3"
    ) 

x, y, z = "MLR"

cort[2] = 11

print(cort[1:3])