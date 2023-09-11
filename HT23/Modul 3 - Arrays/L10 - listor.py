# Genomgång från HT21: https://www.youtube.com/watch?v=lkTwC7rn148&ab_channel=HampusEriksson


# Skapa en lista - square brackets - alt gr + 8
inventory = ["axe", "sword", "shield", "bow", "arrows"]

# len()
print(len(inventory))

# Index - börjar på 0
print(inventory[2])

# Index bakvänt - börjar på -1
print(inventory[-1])

# Lägga till - append
inventory.append("potion")
inventory.append(input("What would you like to add to the inventory?"))

# Ta bort med värde - remove
print(inventory)
inventory.remove("bow")
print(inventory)

# Ta bort alla med värde - list comprehension - lite mer avancerat
inv_test = [item for item in inventory if item != "sword"]

# Ta ut med index - pop
print(inventory)
inventory.pop(0)
print(inventory)

removed_item = inventory.pop(2)

# Sortera
inventory.sort()

# Printa ut listor - använd * unpack
print(*inventory)
print(*inventory, sep=", ")
print(*inventory, sep=", ", end=".!")


# Loopa igenom listor
for item in inventory:
    print(item)

# Loopa igenom listor - enumerate
for index, item in enumerate(inventory, start=1):
    print(f"{index}: {item}")

# Sum, max, min
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(my_numbers))
print(max(my_numbers))
print(min(my_numbers))

# Lista som input
students = input("Name all your students, separated by space: ").split(" ")
print(*students)

# Kolla om något finns i en lista
check = input("What would you like to check? ")


if check in inventory:
    print(f"You have an {check}!")

elif "axe" in inventory:
    print("You have an axe!")  

else:
    print(f"You don't have an {check}!")