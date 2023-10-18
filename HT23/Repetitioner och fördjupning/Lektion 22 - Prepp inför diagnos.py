# Boolean
True
False

# logiska operatorer
==
<
>
<=
>=
!=

# jämförelseoperatorer - and / or / not
1. not
2. and
3. or

# pass - om vi inte vet än vad som ska hända
if age > 5:
    pass

# .lower, .upper, .capitalize
svar = input("Vilket är huvudstaden?").capitalize()

if svar == "Rom":
    print("Rätt")

# if - om något händer - 1 fall
# elif - ett till fall
# else - alla andra fall

# for-loop - specifikt antal gånger, t.ex. en per element i lista

# while-loop - loopar medans något är sant eller break

# i i detta fall kallas loop-variabel
for i in range(10):
    print(i)

# vi kan loopa igenom arrays (listor, tuples, dict, sets)
# vi kan loopa igenom string
# vi kan inte loopa igenom int, float, bool

# range ger ett intervall
# range(start, stop, step)

for i in range(10):
    print(i)

# en bool behövs för att while ska fungera

i = 0
while i < 100:
    i+=1
    if i % 3 == 0:
        continue
    print(i)

# break kan avbryta en while-loop

import random
number = 1
# villkoret checkas varje loop-iteration
while number < 100:
    print(number)
    number = 200
    print(number)
    number=random.randint(1,10)

# loopvariabeln är varje bokstav i strängen
for x in "markus":
    print(x)

# for else - else körs när for-loopen inte har brutits
students = ["Erik", "Vilgot", "Marcus", "Tom", "Daiki", "Egli", "Mattias"]

for student in students:
    if student == "Mattias":
        break

else:
    print("For-loopen breakade inte")