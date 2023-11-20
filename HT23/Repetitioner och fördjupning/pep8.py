# PEP8
# Best practice och guidelines för Python
# Det viktigaste för att skriva bra kod
# är att vara konsekvent, oavsett programmeringsspråk.
# Video med Tech With Tim: https://www.youtube.com/watch?v=D4_s3q038I0&ab_channel=TechWithTim

# Imports - längst upp i filen
import math
import random

# Bra
from random import randint
from datetime import datetime

# Undvik
from random import *
from datetime import *  # Wildcard-importer kan göra det otydligt vilka element som används

# Konstanter - längst upp i filen
# Namngivning - ALL_CAPS för konstanter
WIDTH = 800
HEIGHT = 600
AMOUNT_OF_START_CARDS = 52


# Funktioner - efter konstanter
# Namngivning - snake_case för funktioner och variabler
def area_of_circle(radius):
    return math.pi * kvadrat(radius)


number_of_circles = 3


# camelCase
# Namngivning - PascalCase för klasser
class BigCircle:
    pass


# Indentering - 4 mellanslag
def kvadrat(x):
    return x * x


# Blanksteg/mellanslag för att öka läsbarheten
# Runt operatorer
a = 1
b = 2
c = a + b

# Efter kommatecken
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
lang_mening = """Detta är ett exempel på en lång mening som kanske överskrider 
den rekommenderade radlängden enligt PEP 8."""

# Undvik
detta_ar_ett_exempel_pa_en_mycket_lang_mening_som_overskrider_den_rekommenderade_radlangden_i_PEP_8 = (
    "Undvik överdrivet långa rader då det minskar läsbarheten."
)


# Installera formatter black
# Kolla filen installera_formatter.txt
