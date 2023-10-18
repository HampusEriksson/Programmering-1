import random
from my_awesome_functions import remove_random_element as rem_ran
from karaktär_skreen import load_character as load


# https://www.w3schools.com/python/python_functions.asp
# Skapa funktion
def f(x):
    return x**2 + 5

f5 = f(5)
print(f(5))
print(f5)

# Parametrar - det som skickas in till funktionen
# Datatyper på parametrar
# docstring


bananas= ["Yellow banana", "Long banana", "kokbanan", "Skalad banan"]
rem_ran(bananas)
print(bananas)

def y(x):
    x = 10

x = 5
y(x)
print(x)

x += 5
x = x + 5

# Lambda
# variabelnamn = lambda parameter1, parameter2 : returdata

# def g(x,y):
#     return x*y

g = lambda x,y : x * y

print(g(5,10))


# sortera list av tuples
students = [("Erik", 15), ("Adam", 17), ("Berit", 13), ("Carl", 20), ("David", 10)]

# Sorterar default på index [0]
students.sort()

# Om vi vill sortera på andra index, använd lambda-funktion
students.sort(key=lambda x: x[1])
print(students)
