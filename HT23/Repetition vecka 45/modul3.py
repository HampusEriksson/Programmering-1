"""
Listor
Tuples
Dictionaries
Sets
"""

te22 = ["Erik", "Lukas", "Johan", "Simon", "Tobias"]
na22 = ["Johanna", "Jenny", "Sara", "Sofia", "Tove"]

te22.append("Tobias")

na22.remove("Johanna")
# Skriver ut alla elever i listan te22
for elev in te22:
    print(elev)

for elev in na22:
    print(elev)

ny_elev = input("Vad heter du?")
klass = input("Vilken klass vill du börja i?")
#Lägger till ny_elev i rätt lista
if klass == "te22":
    te22.append(ny_elev)

elif klass == "na22":
    na22.append(ny_elev)

