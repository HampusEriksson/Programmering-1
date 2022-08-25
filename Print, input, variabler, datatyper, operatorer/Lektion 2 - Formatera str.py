

name = input("Hej, vad heter du? ")

print("Välkommen", name)

# Använd inte plus, använd format!
food = input("Hej " + name + " vad gillar du att äta?")

# Använd format, mycket bättre!
# {} skrivs med alt gr + 7
food = input(f"Hej {name} vad gillar du att äta?")


print("Hej", name, "du gillar", food, ".")
print(f"Hej {name} du gillar {food}.")

