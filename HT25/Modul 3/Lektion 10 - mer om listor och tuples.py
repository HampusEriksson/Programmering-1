students = ["Anton", "Bob", "Cecilia", "Darin", "Einar", "George", "Harriet", "Beatrice"]

# len() - antal element i listan
print(f"Det finns {len(students)} studenter i klassen.")

# Sortera
print(*students)
students.sort()
print(*students)

for i in range(10, 24):
    print(i)
# Loopa igenom listor
for namn in students:
    print(namn)

# Loopa igenom listor - enumerate
for index, namn in enumerate(students):
    print(f"{index + 1} : {namn}")

# Loopa med hjälp av index - sämre sätt
for i in range(len(students)):
    print(f"{i + 1} : {students[i]}")


print(max(students))
print(min(students))
favoritnr = [9, 7, 67, 19, 21, 61]
# Sum, max, min
print(sum(favoritnr))
print(max(favoritnr))
print(min(favoritnr))

# Lista som input
frukter = input("Skriv dina favoritfrukter. Skriv , emellan.")
frukter = frukter.split(",")
print(frukter)

# Lista - [] - mutable = kan modifieras - har index
# Tuple - ( ) - immutable = kan ej modifieras - har index
hampus_koordinater = (55.462, 67.893)


