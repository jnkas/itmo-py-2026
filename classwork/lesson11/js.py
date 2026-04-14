import json

obj = {
    "123": 123,
    "abc": "ABC"
}

obj = [obj]

with open("obj.json", "wt") as file:
    json.dump(obj, file, indent=4)

print(obj["123"])
print(json.dumps(obj))