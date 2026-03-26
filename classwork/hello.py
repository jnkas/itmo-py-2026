# print("hello World!")

# # Дополним скрипт, чтобы выводить: Привет, меня зовут Евгений
# # новая строка

# hello = "5"
# hello = 1 + 1

# name = "Евгений"

# print(f"{hello}, меня зовут " + name)


# dict_sample = {
# None: 'coco', 
# None: 'mango'
# }

dict_sample = dict(name='Маша', age={16: True})

for k, v in dict_sample.items():
    print(k, v)


for k in dict_sample.keys():
    print(dict_sample[k])

print(
        dict.fromkeys(['one', 'two', 'three', 'four'])
    )


ggh = dict_sample

ggh["name"] = "Света"

print(dict_sample.items())
df = [{"j": 12}, {True: 11}]

del dict_sample['name']
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }

print(type(df[0]))
print(ggh.get("age", 0))