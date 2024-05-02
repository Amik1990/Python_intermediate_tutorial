import json


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)

# 1. způsob konverze do formátu json


def encode_user(o):   # o zde beru jako objekt. Nemohu klasicky pomoci funkce dumps konvertovat slovnik do json formatu, tak musim pouzit vlastni funkci
    if isinstance(o, User):    # znamená pokud objekt "o" je třídy "User" pak....
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


userJson = json.dumps(user, default=encode_user)
print(userJson)  # {"name": "Max", "age": 27, "User": true}


# 2. způsob zápisu:
from json import JSONEncoder


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJson = json.dumps(user, cls=UserEncoder)
print(userJson)  # {"name": "Max", "age": 27, "User": true}

#  lze zapsat i takto
userJson = UserEncoder().encode(user)
print(userJson)  # {"name": "Max", "age": 27, "User": true}


# Konverze zpátky do formátu python

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct   # i kdyby se nezplnila podmínka if, tak se má vygenerovat slovník


userJson = json.loads(userJson, object_hook=decode_user)
print(user.name)  # Max

















