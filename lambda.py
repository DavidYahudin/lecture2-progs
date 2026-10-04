people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Ravenclow"},
    {"name": "Draco", "house": "Slytherin"}
]


people.sort(key = lambda person: person["name"])

print(people)