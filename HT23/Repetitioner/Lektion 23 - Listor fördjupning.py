# Förra årets genomgång: https://www.youtube.com/watch?v=lkTwC7rn148&ab_channel=HampusEriksson
# arrays - kan lagra flera olika data
import random

# Skapa en lista - square brackets - alt gr + 8
politiker = ["Göran", "Jimmie", "Uffe", "Steffe", "Olof", "Ebba", "Annie"]

# len()
print(len(politiker))

# Index - börjar på 0
print(politiker[2])

# Index bakvänt - börjar på -1
print(politiker[-1])

# Lägga till - append
politiker.append("Saddam")

# Ta bort - remove
politiker.remove("Steffe")

print(politiker)

# Ta ut - pop
skjuten = politiker.pop(3)

# Sortera
politiker.sort()

# Printa ut listor - använd * unpack

print(*politiker)

# slumpa lista - dåligt sätt
politiker[random.randint(0,len(politiker)-1)]

# slumpa lista - bra sätt
random.choice(politiker)

# ta ut random sak från lista
politiker.pop(random.randint(0,len(politiker)-1))
politiker.pop(politiker.index(random.choice(politiker)))

# Loopa igenom listor
for politikperson in politiker:
    print(politikperson)

# Loopa igenom listor - enumerate
for index, politikperson in enumerate(politiker):
    print(f"{index} : {politikperson}")

# Sum, max, min
längder = [168, 183, 172, 300, 60, 183]

print(sum(längder))
print(max(längder))
print(min(längder))
#avg
print(sum(längder) / len(längder))

# operatorer - plus kan användas med listor
print(politiker + längder)



# if in list
if 175 in längder:
    print("Någon i klassen är 175 cm")
else:
    print("Ingen i klassen är 175 cm")

if any(längd > 175 for längd in längder):
    print("Någon i klassen är längre än 175 cm")
else:
    print("Ingen i klassen är längre 175 cm")

if all(längd > 175 for längd in längder):
    print("Alla i klassen är längre än 175 cm")
else:
    print("Alla i klassen är inte längre 175 cm")

# Lista som input - split

barn = input("Skriv namnet på alla dina barn, mellanslag emellan varje barn.").split(" ")
print(barn)