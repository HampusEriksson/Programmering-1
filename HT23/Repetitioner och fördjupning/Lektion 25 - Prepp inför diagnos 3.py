# arrays = listor, tuples, dictionaries och sets
# Array är inte en datatyp i python

# Har index = listor, tuples, dictionaries

# Kan ändras, är mutable = listor, dictionaries och sets
[].append(5)
{}["5"] = 5
{1,2,3}.add(4)
a = 5
# kolla typen
type(a)

# kolla om något är av en typ
a = 5
if isinstance(a, int):
    pass
    


# Lista - [] - mutable = kan modifieras - har index
transport = ["Car", "Plane", "Train", "Bike"]

print(*transport)

# lägga till i en lista
transport.append("Scooter")

# Ta bort med element
transport.remove("Plane")

# Ta bort med index och eventuellt spara
later = transport.pop(0)

# Indexerror = ett index som inte finns
print(transport[-100])

if "Boat" in transport:
    print("Boat is in the list")

transport[0], transport[1] = transport[1], transport[0]

for t in transport:
    print(t)

for index, t in enumerate(transport):
    print(f"{index} : {t}")

students = {"Erik":1, "Markus":2, "Ilias": 5}

for key, value in students.items():
    print(f"{key} : {value}")

for key in students.keys():
    print(key)

for value in students.values():
    print(value)
    

[[{"Vilgot":{1,2,3,[-5, (1,2,3)]}}]]


# Tuples kan användas istället för listor om vi vill ha ett konstant värde
start_pos = (0,0)

# Dictionaries kan anväändas med 2 värden kopplade till varandra
user = ["Kerolos", "Daiki"]
passwords = [1234]


