# Booleans 
# Kan vara True eller False
True
False

# Jämförelser har värdet True eller False
print(5 < 3)

# If else elif
age = int(input("What is your age? "))

if age >= 67:
    print("Du är pensionär.")
elif age >= 18:
    print("Du är myndig")
elif age >= 13:
    print("Du är tonåring")
else:
    print("Du är barn.")

# and
# or
name = input("What is your name? ").capitalize()

if name == "Artemio" or age >= 20:
    print("Du går inte i TEI24A.")

# byta aktiv spelare med if else
# olika värden på variabler med if else
active_player = "Gabriel"

if active_player == "Gabriel":
    active_player = "Najib"
else:
    active_player = "Gabriel"

# Likvärdigt mot:
active_player = "Najib" if (active_player == "Gabriel") else "Gabriel"


# ändra score baserat på svårighetsgrad
score = 0

difficulty = "hard"

score += 10 if (difficulty == "expert") else 5

if difficulty == "expert":
    score += 10
else:
    score += 5

# all

grades = ["A", "B", "A", "C", "F"]

if all(grade == "A" for grade in grades):
    print("Alla har A")
else:
    print("Alla har inte A")

# any
if any(grade == "A" for grade in grades):
    print("Någon har A")
else:
    print("Ingen har A")

# match case
betyg = input("Vad fick du för betyg? ")

match betyg:

    case "A":
        print(20)
    case "C":
        print(15)
    case "E":
        print(10)
    case "F":
        print(0)
    case blablabla:
        print(f"{blablabla} är inte ett betyg")
    





punkt = (0, 5)

match punkt:
    case (0, 0):
        print("Punkten är i origo.")
    case (x, 0):
        print(f"Punkten ligger på X-axeln med värdet {x}.")
    case (0, y):
        print(f"Punkten ligger på Y-axeln med värdet {y}.")
    case (x, y):
        print(f"Punkten ligger någonstans i rymden: X={x}, Y={y}")

data = input("Skriv in något: ")
match data:
        
        case int(nummer):
            print(f"Det är ett heltal: {nummer}")
        case list(element):
            print(f"Det är en lista med {len(element)} objekt.")

        case str(text):
            print(f"Det är en textsträng: {text}")



