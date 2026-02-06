
student1 = "Anna"
student2 = "Erik"
student3 = "Sofia"
student4 = "Lucas"
student5 = "Emma"
student6 = "Oscar"
student7 = "Maja"
student8 = "William"
student9 = "Elsa"
student10 = "Hugo"
student11 = "Alice"
student12 = "Alexander"
student13 = "Linnea"
student14 = "Filip"
student15 = "Ida"
student16 = "Simon"
student17 = "Olivia"
student18 = "Viktor"
student19 = "Ebba"
student20 = "Nils"
student21 = "Cornelis"

# Print all students
print(f"Students: {student1}, {student2}, {student3}, {student4}, {student5}, {student6}, {student7}, {student8}, {student9}, {student10}, {student11}, {student12}, {student13}, {student14}, {student15}, {student16}, {student17}, {student18}, {student19}, {student20}, {student21}")

# Skapa en lista - square brackets - alt gr + 8
inventory = ["Cobble stone", "Golden apple", "Leather shield"]

print(inventory)

# Printa ut listor - använd * unpack
print(*inventory)

# Index - börjar på 0
print(inventory[0])
print(f"Den första saken i ditt inventory är {inventory[0]}")

# Index bakvänt - börjar på -1
print(inventory[-2])


# Lägga till - append
inventory.append("Torch")
inventory.append("Pickaxe")
inventory.append(7)

inventory.append(input("Vad vill du lägga till?"))

item = input("Vad vill du lägga till?")
inventory.append(item)

# Ta bort med värde - remove
if 1 == 1:
    inventory.remove("Golden apple")

print(*inventory)


# Kolla om något finns i en lista
question = input("Vad vill du kolla efter i ditt inventory? ")

if question in inventory:
    print(f"{question} is in the inventory.")
else:
    print(f"{question} is not in the inventory.")







