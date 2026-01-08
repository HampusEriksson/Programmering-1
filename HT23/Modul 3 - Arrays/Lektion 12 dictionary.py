# Tidigare genomgång: https://www.youtube.com/watch?v=e3LL4mSrLMs&ab_channel=HampusEriksson
import random
# Users
# Skapa dictionary
# Key-value pair
users = {"vilgot06": "1234", "hampus": "1234", "johanna": "1234"}

print(users["vilgot06"])

# Lägg till key-value pair
users["erik"] = "1234"
users["egli"] = "1234"

# Ändra value
users["erik"] = "1234!"

# Ta bort - del
del users["erik"]

# Ta bort - pop
deleted_user = users.pop("egli")
print(deleted_user)
print(users)
# .keys()
for key in users.keys():
    print(key)

# .values()
for value in users.values():
    print(value)

# .items()
for key, value in users.items():
    print(key, value)

# loopa igenom dictionary
for key in users:
    print(key)

# Räkna händelser
cointoss = {0: 0, 1: 0}
for _ in range(1000):
    coin_tossed = random.randint(0, 1)
    cointoss[coin_tossed] += 1
    
print(cointoss)