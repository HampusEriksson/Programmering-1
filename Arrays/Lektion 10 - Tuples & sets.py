# Tidigare genomgång: https://www.youtube.com/watch?v=TRw6NQcrO_U&ab_channel=HampusEriksson

# Lista - [] - mutable = kan modifieras - har index

elever = ["Ariful", "Dante", "Elliot", "Lion"]
print(*elever)

elever.append("Diana")
print(*elever)

print(elever[2])

elever.remove("Elliot")
print(*elever)

# Dåligt sätt att göra kopia
elever2 = elever
print(*elever2)

elever2.append("Elliot")

print(*elever)
print(*elever2)

# Bra sätt att göra kopia
elever3 = [x for x in elever]

# Tuple - ( ) - immutable = kan ej modifieras - har index
start_pos = (15, 7, 3, 28, 89)
print(start_pos[0])

# Set - { } - mutable = kan modifieras - har ej index
my_nrs = {1,2,3,4,5,5,5,7, 5}
print(my_nrs)

my_nrs.add(8)
my_nrs.add("Hejsan")
print(my_nrs)

my_nrs.remove(5)
print(my_nrs)

missed_teachers = {"Nurcan", "Peter", "Setayesh", "Björn", "Darin"}
print(*missed_teachers)