# For-loop
# Repetera kod ett visst antal gånger

for _ in range(100):
    print("Fortnite")

# loopvariabeln är x i detta fall
for x in range(10):
    print(x)

# Start, stop, step
for x in range(7, 75):
    print(x)

for y in range(-5, 15, 3):
    print(y)

# Loopa igenom string
name = "Vilgot"
# len() ger dig längden av en sträng eller lista
print(len(name))

for letter in name:
    print(letter)

if "a" in name:
    print("A finns i namnet.")

# Nästlad loop
for a in range(10):
    for b in range(5):
        print(f"a={a} b={b}")