# Array är ett samlingsnamn för listor, tuples, sets och dictionaries
# Array är dock inte en datatyp i sig själv i Python
min_lista = [1,2,3, "fjhadk", ["fajg"], {"a": 18}]
min_tuple = (1,2,3)
min_set = {1,2,3}
min_dict = {"One":1, "Two":2, "Three":3}

# Listor och tuples har index. Dict har strängar som index.
print(min_lista[1])
print(min_tuple[1])
# print(min_set[1])
print(min_dict["One"])

# List, sets och dictionaries kan ändras - de är mutable
# Tuples kan inte ändras - de är immutable

# Lägga till
# Lägg till på index med insert - skriver inte över
min_lista.insert(1, 4)
print(min_lista)

# Lägg till i slutet med append
min_lista.append(5)
print(min_lista)

# Ta bort
# Ta bort sista
det_som_togs_bort = min_lista.pop()

# Ta bort via index - index 2 i detta fall
min_lista.pop(2)

# Ta bort via värde
min_lista.remove(1)

# Loopa igenom lista/tuple/sets
for nr in min_set:
    print(nr)

# Loopa igenom med enumerate
for index, nr in enumerate(min_lista):
    print(index, ":",nr)

# Loopa igenom keys
for i in min_dict.keys():
    print(i)

# Loopa igenom values
for i in min_dict.values():
    print(i)

# Loopa igenom keys och values
for i, j in min_dict.items():
    print(i, j)

# Vi kan blanda datatyper i en array i Python

# Tuples - Kan inte ändras, är konstant. Listor kan ändras
# Dictionaries - För att spara två värden kopplade till varandra samtidigt.

# SKriv ut snyggare. Unpacka med *
print(*min_lista)

# Indexerror - Anger ett större index än vad som finns i listan
# print(min_lista[50])
# print(min_dict["fadgfask"])

# Kolla om något, i detta fall "Lion", finns i listan
if "Lion" in min_lista:
    print("Lion finns i listan")

print("Lion" in min_lista)

x = 5
while x > 3:
    print("x störra än 3")
    
while True:
    pass
print(x > 3)

# Byt plats på två element i en lista
min_lista[1], min_lista[2] = min_lista[2], min_lista[1]

min_lista[1] = min_lista[2]
min_lista[2] = min_lista[1] 

a, b, c = 6, 90, 3
a = b # a blir 90
b = a # b blir 90