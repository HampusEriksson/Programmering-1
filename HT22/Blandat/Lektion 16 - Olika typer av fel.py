# Syntaxfel
# print "Ariful"
print("Ariful")

# NameError - om vi refererar till variabel innan deklaration
age = int(input("What is your age? "))
print(age)

# Indenteringsfel - Fel med indentering
for i in range(10):
    print("Hej")
    print("Då")
    if "Ariful" == "Alec":
        print("Hejsan")

print("Nu är jag ute från loopen")

# ModuleNotFoundError - Hittar inte en modul
# import minecraft

# IndexError - Index finns inte
# Har index: Lista, string, tuple
elever = ["Diana", "Omar", "Lucia"]

# print(elever[19])

# KeyError - Hittar inte key i dictionary
elev_betyg = {"Isak":"A", "Dante":"F", "Yassin":"G"}
#print(elev_betyg["Ariful"])
måsvingar = "{ }"
print(f"{måsvingar} ")

# TypeError - Fel med datatyper
print(5 + 10.5)