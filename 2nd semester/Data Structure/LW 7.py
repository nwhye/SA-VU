import json
import os


dictionary = {
    "Artem": "Full-time",
    "Ivan": "Full-time",
    "Egor": "Part-time",
    "Ihor": "Part-time",
    "Bohdan": "Part-time",
    "Oleg": "Full-time",
    "Daniil": "Full-time"
}

json_obj = json.dumps(dictionary, indent=4)

with open("sample.json", "w") as file:
    file.write(json_obj)


with open("sample.json", 'r') as file:
     json_obj = json.load(file)

for name, stat in json_obj.items():
    if stat == "Full-time":
        print(name)
