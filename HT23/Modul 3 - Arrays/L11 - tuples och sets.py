# Tidigare genomgång: https://www.youtube.com/watch?v=TRw6NQcrO_U&ab_channel=HampusEriksson

# Lista - [] - mutable = kan modifieras - har index
students = ["Kokchun", "Tommy", "Marcus", "Simon", "Tatiana", "Herman", "Tobias", "Linus"]

students.remove("Kokchun")
students.append("Erik")
print(students[0])

# Tuple - ( ) - immutable = kan ej modifieras - har index
my_favorite_fruits = ("apple", "banana", "orange")
start_position = (0, 0, 0)

print(my_favorite_fruits[0])


# Set - { } - mutable = kan modifieras - har ej index
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set.add(10)
print(my_set)
my_set.add(10)
print(my_set)

for nr in my_set:
    print(nr)

# Ta bort dubletter ur lista
my_list = [1, 2, 3, 3, 4, 5, 5, 5, 6, 7]
my_list = set(my_list)
my_list = list(my_list)

# Dåligt sätt att göra kopia
fruits = ["apple", "banana", "orange"]
fruits_copy = fruits
fruits_copy.append("melon")
print(fruits)

a = 5
b = a
b += 5
print(a)

# Bra sätt att göra kopia
fruits = ["apple", "banana", "orange"]
fruits_copy = fruits.copy()
fruits_copy.append("melon")
print(fruits)

# Eller
fruits = ["apple", "banana", "orange"]
fruits_copy = fruits[:]
fruits_copy.append("melon")
print(fruits)

# eller
fruits = ["apple", "banana", "orange"]
fruits_copy = [fruit for fruit in fruits]
fruits_copy.append("melon")
print(fruits)

# eller
fruits = ["apple", "banana", "orange"]
fruits_copy = []
for fruit in fruits:
    fruits_copy.append(fruit)
fruits_copy.append("melon")
print(fruits)

# eller
fruits = ["apple", "banana", "orange"]
fruits_copy = []
for i in range(len(fruits)):
    fruits_copy.append(fruits[i])
fruits_copy.append("melon")
print(fruits)

# eller
fruits = ["apple", "banana", "orange"]
fruits_copy = []
i = 0
while i < len(fruits):
    fruits_copy.append(fruits[i])
    i += 1
fruits_copy.append("melon")
print(fruits)

