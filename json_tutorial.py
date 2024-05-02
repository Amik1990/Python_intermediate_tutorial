import json

person = {"name": "John", "age": 30, "city": "New York", "hasChidldren": False, "titles": ["engineer", "programmer"]}

# Konverze do json formátu
personJson = json.dumps(person, indent=4, sort_keys=True)   # zkonvertuje do json formátu. Indent rozhodí obsah do řádků. Bez indent bych to bylo v jednom řádku
# print(personJson)       # sort_keys utřídí obsah abecedně

# Vytvoření json souboru person.json
with open("person.json", "w") as file:
    json.dump(person, file)    # Mohu zde taky pouzit indent

person = json.loads(personJson)   # opět vráti slovník do python formátu
print(person)   # {'age': 30, 'city': 'New York', 'hasChidldren': False, 'name': 'John', 'titles': ['engineer', 'programmer']}

