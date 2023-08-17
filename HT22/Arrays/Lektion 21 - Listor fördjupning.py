# Förra årets genomgång: https://www.youtube.com/watch?v=lkTwC7rn148&ab_channel=HampusEriksson
# arrays - kan lagra flera olika data
import random

# Skapa en lista - square brackets - alt gr + 8
my_fav_nrs = [5, 7, 69, 420, 2, 666]

# len()
print(len(my_fav_nrs))

# Index - börjar på 0
print(my_fav_nrs[2])
print(my_fav_nrs[5])

# Index bakvänt - börjar på -1
print(my_fav_nrs[-1])

# Lägga till - append
my_fav_nrs.append(12)

# Ta bort - remove
my_fav_nrs.remove(5)
print(my_fav_nrs)
# Ta ut - pop
removed_nr = my_fav_nrs.pop(2)
print(my_fav_nrs)

# Sortera
my_fav_nrs.sort()
print(my_fav_nrs)

# slumpa lista
random.shuffle(my_fav_nrs)
print(my_fav_nrs)

# Printa ut listor - använd * unpack
print(*my_fav_nrs)
print(*my_fav_nrs, sep=", ")

# Loopa igenom listor
for nr in my_fav_nrs:
    print(nr)

# Loopa igenom listor - enumerate
for index,nr in enumerate(my_fav_nrs):
    print(index, nr)

# Sum, max, min
print(sum(my_fav_nrs))
print(max(my_fav_nrs))
print(min(my_fav_nrs))

# operatorer
print([1,2,3] + [4,5,6])
#print([1,2,3] / [1,2,3])

# if och listor

if 5 not in my_fav_nrs:
    print(5, "finns inte i listan")

# Lista som input
namn = input("Skriv olika namn, separera med mellanslag").split(" ")
print(namn)