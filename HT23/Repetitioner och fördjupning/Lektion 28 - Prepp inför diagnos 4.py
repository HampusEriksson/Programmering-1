# Prepp inför diagnos 4

# En modul/bibliotek är separata funktioner
# Som ligger någonstans inbyggt/pip install
import random, sys, math, pygame, time
from random import choice

random.randint(1,10)
choice([1,2,3,])

# Imports ska ske längst upp

# Vad är en funktion?
# En funktion är en fördefinierad instruktion som vi kan använda flera gånger

# En parameter är något som skickas in till funktionen
# I detta fall x och y
# y är en default parameter, om den inte skickas in blir y = 2
def f(x, y=2):
    return x**y


print(f(5, 3))

# En funktion måste inte ha parametrar

def hello():
    print("Hello world")

print(hello())

# Man kan ha funktionerna i en annan fil för att hitta
# Bättre struktur, kortare namn osv. enklare att använda

# TypeError
print("5" + 5)

# SyntaxError
print("hej"
      
# NameError
print(name)

for i in range():
print(10)