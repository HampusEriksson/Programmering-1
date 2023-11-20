import sys


def hall(karaktär):
    print(
        """Du är i en hall. Det finns en dörr till vänster och en dörr till höger.")
    Vad gör du?")
    1. Går till vänster")
    2. Går till höger")
    3. Går tillbaka"""
    )
    val = input("Välj: ")
    if val == "1":
        return "matsal"
    elif val == "2":
        return "kök"
    elif val == "3":
        return "utanför"
    else:
        print("Det förstod jag inte. Försök igen.")
        hall()


def utanför(karaktär):
    print(
        """Du är utanför slottet. Det finns en dörr framför dig.")
    Vad gör du?")
    1. Går in genom dörren")
    2. Springer hem till mamma"""
    )
    val = input("Välj: ")
    if val == "1":
        return "hall"
    elif val == "2":
        print("Du springer hem till mamma")
        sys.exit()
    else:
        print("Skriv 1 eller 2")


def matsal(karaktär):
    print(
        """Du är i en matsal. Det finns en dörr till höger.")
    Vad gör du?")
    1. Går till höger")
    2. Går tillbaka"""
    )
    val = input("Välj: ")
    if val == "1":
        return "hall"
    elif val == "2":
        return "matsal"
    else:
        print("Skriv 1 eller 2")


def kök(karaktär):
    print(
        """Du är i ett kök. Det finns en dörr till vänster.")
    Vad gör du?")
    1. Går till vänster")
    2. Går tillbaka"""
    )
    val = input("Välj: ")
    if val == "1":
        return "hall"
    elif val == "2":
        return "kök"
    else:
        print("Skriv 1 eller 2")


karaktär = {
    "namn": "Kalle",
    "hp": 100,
    "skada": 20,
    "försvar": 10,
    "vapen": "svärd",
}

position = "utanför"

while True:
    if position == "utanför":
        position = utanför(karaktär)
    elif position == "hall":
        position = hall(karaktär)
    elif position == "matsal":
        position = matsal(karaktär)
    elif position == "kök":
        position = kök(karaktär)
