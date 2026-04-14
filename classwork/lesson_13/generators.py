from string import ascii_letters

letters = 'hыtφтrцзqπ'

print(ascii_letters)

# isEng = [f'{letter} - ДА' if letter in ascii_letters 
#          else f'{letter} - НЕТ' 
#          for letter in letters]

print([f'{letter} - ДА' if letter in ascii_letters 
         else f'{letter} - НЕТ' 
         for letter in letters])

list1 = [x**2 for x in range(0, 50) if x%3 == 0]
# print(list1)

def func(item):
    if item in ascii_letters:
        return item
    else:
        return ""


print([func(letter) for letter in letters])

for word in ['Я', 'изучаю', 'Python']:
    print("word: " + word)

    for letter in word:
        print("letter: " + letter)

# for i in {"sad": "asd111"}:
#     print({"sad": "asd111"}[i])

matrix = [[i for i in range(0, 10)] for j in range(0, 10)]
# print(matrix)
        

arr = ['cat', 'dog', 'cow']

dict1 = {}

for item in arr:
    if item == "cat":
        dict1[item] = "мяу"
    elif item == "dog":
        dict1[item] = "гав"

print(dict1.items())

dict2 = {item: "" for item in arr}

print(dict2)


names = ['Harry', 'Hermione', 'Ron', 'Neville', 'Luna']
index = {
    k:v for (k, v) in enumerate(names)
}
print(index)
{'Harry':0, 'Hermione':1, 'Ron':2, 'Neville':3, 'Luna':4}