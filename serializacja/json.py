from serializacja.obj_to_serialize import *


slownik = {
    'a': 903812,
    'b': (2, 3, 4),
    'c': "1234567890",
    'd': [1, 2, 3, 4, 5],
    'e': {"123": "456"}
}

go = Cla()

jsony = []

for key, value in slownik.items():
    j = json.dumps(value)
    jsony.append(j)
    print(j, type(j))


jgo = json.dumps(go.__dict__)
jsony.append(jgo)
print(jgo, type(jgo))


print('-' * 100)


for j in jsony:
    j = json.loads(j)
    print(j, type(j))
