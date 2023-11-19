# PEP8

# Imports - längst upp i filen
import math

# Bra
from datetime import datetime

# Undvik
from modul import *  # Wildcard-importer kan göra det otydligt vilka element som används


# Indentering - 4 mellanslag
def kvadrat(x):
    return x * x

# Namngivning - snake_case för funktioner och variabler
def area_of_circle(radius):
    return math.pi * kvadrat(radius)

number_of_circles = 3

# Namngivning - PascalCase för klasser
class Circle:
    pass

# Namngivning - ALL_CAPS för konstanter
WIDTH = 800
HEIGHT = 600

# Blanksteg för att öka läsbarheten
# Runt operatorer
a = 1
b = 2
c = a + b

# Runt kommatecken
numbers = [1, 2, 3]

# Kommentarer
# Kommentarer bör vara tydliga och koncisa, förklara komplex logik eller ge sammanhang.

# Bra
# Beräkna arean av en rektangel
def rakna_area(langd, bredd):
    return langd * bredd

# Undvik
# Denna funktion multiplicerar längd och bredd
def area(l, b):  # Otydliga parameterbeteckningar
    return l * b

# Att hålla raderna rimligt korta (helst under 79 tecken) förbättrar läsbarheten.
# Bra
lang_mening = "Detta är ett exempel på en lång mening som kanske överskrider den rekommenderade radlängden enligt PEP 8."

# Undvik
detta_ar_ett_exempel_pa_en_mycket_lang_mening_som_overskrider_den_rekommenderade_radlangden_i_PEP_8 = "Undvik överdrivet långa rader då det minskar läsbarheten."




