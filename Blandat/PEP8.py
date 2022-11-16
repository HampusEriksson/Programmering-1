# PEP8 - Hur man skriver kod "rätt"
import random

# Installera en formater. Det är typ som att ha ett automatiskt rättstavningsprogram
# Klicka på terminal längst upp, sen ny terminal
# Skriv pip install black i terminalen
# Om det inte funkar testa: python -p pip install black
# Om det inte funkar testa: python3 -p pip install black
# Om det inte funkar testa: ge upp
# Gå in i settings, kugghjul nere till vänster
# Sök på python format provider
# Välj black i listan
# Sök på format
# Se till att "Editor: Format On Save" är iklickad


# Indentation = 4 spaces
# Klicka längst ner där det står spaces/tab size. Välj "Indent using spaces" och sen 4.

# Det viktigaste av allt - VAR KONSEKVENT
# Citattecken - är likvärdiga - använd endast en av dessa!
"Dante"
"Dante"

# Parenteser - antingen på alla eller inga jämförelser
if x > 5:
    pass

elif x == 5:
    pass

# Max 80 characters per line
min_lista = [
    "aaaa",
    "aaaa",
    "aaaa",
    "aaaa",
    "aaaa",
    "aaaa",
    "aaaa",
    "aaaa",
    "aaaa",
    "aaaa",
    "aaaa",
]

# variabler - snake_case - små bokstäver - eventuellt mellanrum skrivs med _

player_name = "Dante"
player1 = "Dante"
first_name = "Dante"

# camelCase

# PascalCase

# konstanter - ALLCAPS
STARTPOS = (50, 75)

# filer - snake_case
# modules - snake_case
# t.ex.: rock_paper_scissors.py

# functions - snake_case
def spam():
    pass


# class - PascalCase
class MyClass:
    pass


# exceptions - PascalCase
SyntaxError

# imports - längst upp

# whitespaces
# fel: spam( ham[ 1 ], { eggs: 2 })
spam(ham[1], {eggs: 2})  # rätt
# spam (3)
spam(3)
# i=i+1
i = i + 1
# i +=1
i += 1
# a = (5 + 5) * (5 + 5)
a = (5 + 5) * (5 + 5)

# default värden i funktioner - ingen blankspace
def spam2(x=5):
    pass


# inline comment - 2 spaces före comment, en space efter, börja med stor bokstav
student = "Eddie"  # Coolaste studenten nocap

# if student[:3] == "bar"
if student[:3] == "Edd":
    print("Börjar med Edd")

if student.startswith("Edd"):
    print("Börjar med Edd")
