# For-loop
# Repetera kod ett visst antal gånger
"""
for _ in range(100):
    print("Hej")

# Repetera kod med variabel
for i in range(100):
    print(i)

# Start, stop, step
for i in range(0, 101, 2):
    print(i)

for i in range(100, 0, -1):
    print(i)

# Loopa igenom string
name = "Oskar"

for letter in name:
    print(letter)


# Nästlad loop

for x in range(10):
    for y in range(10):
        print("x: ", x, "y: ", y)

"""

# Break

for _ in range(100):
    name = input("What is your name? ").capitalize()
    if name == "Batin":
        break