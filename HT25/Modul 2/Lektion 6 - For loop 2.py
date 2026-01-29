# For-loop
# Repetera kod ett visst antal gånger
for _ in range(100):
    print("Var är Gabriel???")


# loopvariabel

for i in range(100):
    print(i)

# Start, stop
for i in range(67, 78):
    print(i)
# Start, stop, step
for i in range(100, 1000, 2):
    print(i)


# Loopa igenom string
# En string är en iterable

namn = "Kårnäulius"

for bokstav in namn:
    print(bokstav)

# len() ger dig längden av en sträng eller lista
print(f"Namnet {namn} är {len(namn)} tecken långt.")

