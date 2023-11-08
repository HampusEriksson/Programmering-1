"""
If-satser
For-loopar
While-loopar
Booleans
Jämförelser
"""

# If-satser
while True:
    age = int(input("Ange din ålder. Skriv 0 för att avsluta: "))

    if age == 0:
        break

    elif age >= 18:
        print("Du är vuxen.")

    else:
        print("Du är ett barn.")

while True:
    bäst = input("Vem är bäst? ").capitalize()
    if bäst == "Ayoob" or bäst == "Alex":
        print("Rätt svar!")
        break
    if bäst in ("Ayoob", "Alex"):
        print("Rätt svar!")
        break
    else:
        print("Fel svar!")

# Här hamnar vi efter att while breakas
print("Programmet avslutas.")

# For-loopar
for i in range(10):
    print(i)

for x in range(1, 11):
    print(x)

for y in range(100, 375, 3):
    print(y)