# Byta plats på två värden
nummer = [1,2,3,4]

# Använd temporär variabel
t = nummer[0]
nummer[0] = nummer[2]
nummer[2] = t

# Gör på en och samma rad
a,b,c = 1,6,42
nummer[0], nummer[2] = nummer[2], nummer[0]

nummer = []
for i in range(1,101):
    nummer.append(i)

# list comprehension
nummer = [i for i in range(1,101)]
print(nummer)

even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)
# lista som parameter i funktion
def change(x):
    print(f"värdet i funktionen: {x}")
    x[0] = 77
    print(f"värdet i funktionen: {x}")


a = [1,2,3]
change(a)
print(a)

# Kopia av lista
inventory = ["Apple", "Sword"]
# Felaktigt sätt att kopiera lista
inventory2 = inventory
# Rätt sätt 1 att kopiera lista
inventory2 = inventory.copy()
# Rätt sätt 2 att kopiera lista
inventory2 = [item for item in inventory]

inventory2.append("Shield")
print(*inventory)


nummer = [i for i in range(1,101)]

# Slice
# [start:stop:step]
print(nummer[3:17:4])
print(nummer[:len(nummer)//2])


# Lista som input - split
favoriter = input("Skriv alla dina favoriter, separara med mellanslag").split(" ")
print(favoriter)