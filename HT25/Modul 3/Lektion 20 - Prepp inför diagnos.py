# Hur vet datorn vilken kod som ska köras när en if-sats blir sann?

age = 38
if age > 25:
    print("Det här körs om age > 25")
    print("Det här körs också om age > 25")

print("Det här körs alltid")

# Vad heter datatypen som är relevant när vi pratar om if-satser och jämförelser?
# Vilka värden kan datatypen i fråga 2 anta?
# Boolean
True
False

# Vilka jämförelseoperatorer och logiska operatorer har vi i python?
# jämförelseoperatorer
# ==
# >=
# >
# <=
# <
# !=

# Logiska operatorer
# and
# or
# not

# I vilken ordning prioriteras de logiska operatorerna?
# not and or
x = True or False and False
print(x)

level = 10
gold = 5000

if level >= 10 or (level >=8 and gold > 1000):
    print("Kom in")

# If-satser kan inte vara tomma, vad skriver vi för att göra koden körbar ändå?
if level < 10:
    # Fixa det här sen
    pass

# Hur är metoder som .lower(), upper() och .capitalize() 
# relevant när vi pratar om if-satser? 
# Förklara och/eller ge exempel

svar = input("Vem är den bästa fysikläraren?").lower()

if svar == "sidar":
    print("fel")

# Beskriv skillnaden mellan if, elif och else.
# När används elif?
# if används först
if svar == "mario":
    print("Rätt")
# elif flera alternativ
elif svar == "kadir":
    print("Nästan rätt")
elif svar == "hampus":
    print("inte fysiklärare xD")
# else den sista, samlar in resten
else:
    print("det du skrev finns inte i ens som svar...")

# Beskriv kort skillnaden på en while- och en for-loop.
password = "123"
test = input("skriv in lösen")

while test != password:
    test = input("fel, skriv in lösen")


# Vad kallas variabeln du skapar i en for-loop?
for i in range(100):
    # i kallas i detta fall för loopvariabel
    print(i)

# Vilka datastrukturer kan vi for-loopa igenom (iterera över)?

for char in "omar":
    print(char)

# Vi kan även loopa över lista, dictionary, tuple

# Vad gör range-funktionen?
# Vad blir skillnaden på range om du har en, två eller tre parametrar?
for i in range(100):
    print(i)
for i in range(50,100):
    print(i)
for i in range(20,100, 4):
    print(i)

# Vad gör att while-loopar fungerar? Vad krävs?
# en jämförelse
while True:
    print("Infinite print")
    break

# Vad gör nyckelordet continue?
# hoppar till nästa loop

# Vad gör nyckelordet break?
# bryter loopen

# När kontrolleras villkoret i en while-loop?
password = "123"
test = input("skriv in lösen")

while test != password:
    test = input("fel, skriv in lösen")
    print("Kommer detta skrivas ut om man skriver 123 på raden ovan?")


# Hur fungerar for-else? Dvs else kopplat till en for-loop
# for-else körs endast om for-loopen bryts