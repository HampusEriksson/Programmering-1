# Förra årets genomgång: https://www.youtube.com/watch?v=lkTwC7rn148&ab_channel=HampusEriksson

# Skapa en lista - square brackets - alt gr + 8
from curses.ascii import isdigit


mobiler = ["iPhone 14", "One plus", "Blackberry", "Samsung 22"]

# len()
print(len(mobiler))
# Index - börjar på 0
print(mobiler[3])

# Index bakvänt - börjar på -1
print(mobiler[-1])

print(mobiler)
# Lägga till - append
mobiler.append("Huwaei")
print(mobiler)
# Ta bort - remove
mobiler.remove("One plus")
print(mobiler)

# Ta ut - pop
en_mobil = mobiler.pop()
print(en_mobil)

# Sortera
mobiler.sort()

# Printa ut listor - använd * unpack
print(*mobiler, sep=", ")

# Loopa igenom listor
for mobil in mobiler:
    print(mobil)

# Loopa igenom listor - enumerate
for i, mobil in enumerate(mobiler, start=1):
    print(i, mobil)

# Sum, max, min
fav_nrs = [218962,521528152,15,51252185,512,521512]
print(sum(fav_nrs))
print(max(fav_nrs))
print(min(fav_nrs))

# Lista som input
fav_foods = input("Vad är dina favoriträtter? Separera med mellanslag. ").split(" ")
print(fav_foods)


# bonus - isdigit()
siffra = input("Siffra??")

if siffra.isdigit():
    siffra = int(siffra)