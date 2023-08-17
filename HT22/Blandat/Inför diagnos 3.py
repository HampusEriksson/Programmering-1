import random
from turtle import onscreenclick


if 5 > 3:
    print("Den här koden kommer köras om jämförelsen är sann")

print("Den här koden körs alltid")

# Booleans - Antingen True eller False
True
False
"""
and
or
not
<
>
<=
>=
!=
==
"""

if True and False or True:
    print("and körs först")

# and körs först, innan or

def kick_user(user):
    pass

svar = input("Vem är bäst?").capitalize()

# if elif else är kopplade till varandra

if svar == "Hampus":
    print("Rätt no cap")

elif svar == "Mohammad":
    pass

elif svar == "Dante":
    pass

else:
    pass


# For
# i i detta fall kallas loopvariabel eller iterator
range(10) # från 0 till 10
range(10, 15) # från 10 till 15
range(25, 68, 2) # varannat tal från 25 till 68

for i in range(10):
    print(i)

# Vi kan loopa igenom alla typer av arrays och strängar

for elev in ["Eddie", "Ariful", "Isak"]:
    print(elev)

for bokstav in "Oskar":
    print(bokstav)

# While
"""
while True:
    pass
"""

age = 0
while age > 25:
    age += 1
    print(age)


i = 0
# i < 100 kontrolleras när loopen kommer tillbaka till start
# kontrolleras inte under körning
while i < 100:
    i += 1
    if i % 3 == 0:
        continue
    print(i) # Detta körs endast om continue inte har körts ovan

i = 0
while i < 100:
    i += 1
    if i % 3 != 0:
        print(i)


students = ["Batin", "Alec", "Yassin", "Diana", "Lion", "Hundaol", "Rasmus", "Lucia", "Robert", "Isak"]

# For else
for index, student in enumerate(students):
    if random.random() <= 0.1:
        print(f"{student} got kicked from the class. Impostor replaces.")
        students[index] = "Impostor"
        break
    else:
        print(f"{student} gets to stay in the class.")

# else körs om break inte körts i for-loop ovan
else:
    print("Noone got kicked from the class.")