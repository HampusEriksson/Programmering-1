# Repetition

# Onödiga steg i if-satser
score = 75
if score >= 90:
    print("Betyg: A")
elif score >= 80 and score < 90: 
    print("Betyg: B")
elif score >= 70 and score < 80: 
    print("Betyg: C")
elif score >= 60 and score < 70: 
    print("Betyg: D")
elif score >=50 and score<60:
    print("Betyg: E")
elif score < 50:                 
    print("Betyg: F")

# Förbättrat sätt
score = 75
if score >= 90:
    print("Betyg: A")
elif score >= 80: 
    print("Betyg: B")
elif score >= 70: 
    print("Betyg: C")
elif score >= 60: 
    print("Betyg: D")
elif score >=50 :
    print("Betyg: E")
else:                 
    print("Betyg: F")

# Range - hur funkar den egentligen?

for x in range(10):
    print(x)

for y in range(4,22):
    print(y)

for z in range(5,60, 5):
    print(z)

# While loop

rätt_svar = "Magnus"
while True:
    svar = input("Vem är bästa läraren?")
    svar = svar.capitalize()
    if svar == rätt_svar:
        print("Rätt")
        break
    else:
        print("Fel, try again!")

tries = 0
score = 0
while tries < 3:
    svar = input("Vem är bästa läraren?")
    svar = svar.capitalize()
    if svar == rätt_svar:
        print("Rätt")
        score += 1
        break
    else:
        tries += 1
        print(f"Fel, try again! Du har {3-tries} gissning kvar.")
