# Booleans 
# Kan vara True eller False
True
False

# Jämförelser har värdet True eller False
print(5 > 3)

print(6>10)

# If else elif

age = int(input("Hur gammal är du? "))
if age >= 18:
    print("Du är vuxen")
elif age >= 15:
    print("Du är tonåring")
elif age >= 10:
    print("Du är barn")
else:
    print("Du är bebis")

# and
# or
ayob_age = 19
ayob_attribute = "g"
nr_of_girls = 120
krogen_brinner = False
if (ayob_age>=18 and ayob_attribute=="g" and nr_of_girls>100) or krogen_brinner:
    print("Du får gå på krogen")
else:
    print("Du får inte gå på krogen")

# byta aktiv spelare med if else
# olika värden på variabler med if else
active_player = "Ayob"

# byt aktiv spelare
if active_player == "Ayob":
    active_player = "Erik"
else:
    active_player = "Ayob"

# bättre sätt
active_player = "Erik" if active_player == "Ayob" else "Ayob"

score = 0
difficulty = "hard"
score += 10 if difficulty == "hard" else 5


# all
# any
students_grades = [10, 10, 10, 10, 10, 5, 3, 10, 10, 10]
if any(grade == 3 for grade in students_grades):
    print("Någon fick 3")

if all(grade == 10 for grade in students_grades):
    print("Alla fick 10")
else:
    print("Någon fick ett betyg som inte var 10")

# match case
grade = input("Vilket betyg kommer du få i Engelska 6?")

match grade:

    case "A":
        print("Du fick A")
    case "B":
        print("Du fick B")
    case "C":
        print("Du fick C")
    case "D":
        print("Du fick D")
    case "E":
        print("Du fick E")
    case "F":
        print("Du fick F")
    case _:
        print("Du fick ett betyg som inte var A, B, C, D, E eller F")





