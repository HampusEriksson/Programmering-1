# Man kan lägga sina funktioner i en annan fil så att alla
# funktioner är på samma plats
# T.ex. lättare att få översikt
# Här importerar jag func_in_file från filen/modulen minafunktioner.py
from minafunktioner import func_in_file

# Allting vi importerar är från en modul
# Import ger oss tillgång till modulen
# Vi importerar moduler längst upp i programmet
import random, pygame, turtle, time, tkinter, math, os, sys

# En funktion är en bit kod som används genom att kalla på den
# Används t.ex. för att slippa återupprepa kod
# En funktion ska göra en sak, och göra den saken bra

# En parameter är det som skickas in i funktionen, i detta fall x
# Default parameter används om inte parametern skickas in
# Om inte ett värde för y skickas in, blir y = 2
# "Vanliga" parametrar måste skrivas innan default parametrar
def f(x, y= 2):
    return x ** y

# En funktion behöver inte ha parametrar
# Ingenting behöver returneras från en funktion
def game():
    print("Här körs spelet")

svar = f(5)
print(svar)

svar2 = f(8, 3)
print(svar2)

# Om inte return används i funktionen returneras None by default
svar3 = game()
print(svar3)