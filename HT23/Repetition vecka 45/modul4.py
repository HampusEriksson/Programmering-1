"""
Funktioner
Bibliotek
De vanligaste felen
"""
# Funktioner

def hello():
    print("Hello")

hello()

def hello_name(name):
    print(f"Hello {name}.")

hello_name("Markus")
hello_name("Ayob")

def sub(a, b):
    print(a-b)

sub(13, 5)
sub(100, 99)

def fix(name):
    return "Kamrat " + name.capitalize()

namn = fix("ayob")
print(namn)

namn2 = fix("daiki")
print(namn2)


# Ett tal är jämnt om tal % 2 == 0

# Bibliotek - Något vi måste importera

import random

random.randint(1,100)

# Syntax error - när vi har rött under
print("Hello world"
      
# NameError
print(my_name)

# IndentationError
if namn == "Hampus":
print("Coolt")