# Booleans 
# Kan vara True eller False
# Jämförelser har värdet True eller False
import time


print(5 > 5)

# If else elif
name = input("Name? ").capitalize()

if name == "Orvar":
    print("Hej")

elif name == "Lion":
    print("Print ariful")

elif name == "Andhrew tate":
    print("Usch")

else:
    print("Inget fall fanns")

# and
# or
age = 5
if age == 5 and name == "Peter":
    print("nånting")
"""
# if else i variabeldeklaration
active_player = "X"

while True:
    time.sleep(1)
    # Här körs en runda
    if active_player == "X":
        active_player = "Y"

    elif active_player == "Y":
        active_player = "X"

active_player = "X"

while True:
    time.sleep(1)
    # Här körs en runda
    active_player = "X" if active_player == "Y" else "Y"

"""
# match case

name = input("Name? ").capitalize()

match name:

    case "Orvar":
        print("Hej orvar")

    case "Oskar":
        print("Hej oskar")




