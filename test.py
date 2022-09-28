# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna
def namnet_på_funktionen(parameter1, saksomskickasin2):
    # här skrivs allt som görs
    return parameter1 * saksomskickasin2

result = namnet_på_funktionen(5, 10)
print(result)

def best(name):
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
    print(f"{name} är bäst.")

best("Arda")
best("Dante")

def square(number):
    return number ** 2

num5 = square(5)
print(num5)
square(7)
square(9)

name = input("What is your name? ")

def sums(a, b):
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
    pass


# Nu blir det lite svårare


def maximum(a, b, c):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    pass


def palindrom(ord):
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    pass


def prime(nr):
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut
    pass
