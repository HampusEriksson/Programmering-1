# Tidigare genomgång: https://www.youtube.com/watch?v=e3LL4mSrLMs&ab_channel=HampusEriksson

# Users
# Skapa dictionary
# Key-value pair

users = {"alec.andin" : "1234", "eddie.sunden" : "nocap", "adam" : "adam123", "berit" : "berit123", "carl":"carl123"}

print(*users)

# Lägg till key-value pair
users["dante.norling"] = "aaahh"
print(*users)

# Ändra value
users["dante.norling"] = "surprised look"

# Ta bort - del
del users["dante.norling"]

# Ta bort - pop
users.pop("alec.andin")

print(*users)

"""
logged_in = False

while not logged_in:

    username = input("Username: ")
    password = input("Password: ")

    if users[username] == password:
        print("Logged in.")
        logged_in = True

    else:
        print("Username or password is incorrect.")

"""

# .keys()
for x in users.keys():
    print(x)

# .values()
for x in users.values():
    print(x)

# .items()
for x, y in users.items():
    print(x, y)

# Räkna
import random

counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for _ in range(1000):
    slump = random.randint(1,6)
    counts[slump] += 1

print(counts)





