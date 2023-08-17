# Felhantering
# Se till att programmet inte kraschar
# Krav för A

""" Detta skapar problem
bankroll = 69000
bet = int(input("How much do you want to bet?"))
bankroll -= bet"""

# Lösning 1 - while-loop och isdigit

bankroll = 69000
while True:
    bet = input("How much do you want to bet?")
    if bet.isdigit():
        bet = int(bet)
        bankroll -= bet
        break
    else:
        print("Please enter a number")

# Lösning 2 - while, walrus, isdigit

bankroll = 69000
while not (bet := input("How much do you want to bet?")).isdigit():
    print("Please enter a number")

bet = int(bet)
bankroll -= bet

# Lösning 3 - cry and give up

# Lösning 4 - fry and add ketchup

# Lösning 5 - try except

bankroll = 69000
while True:
    try:
        bet = int(input("How much do you want to bet?"))
        bankroll -= bet
        break

    except ValueError:
        print("You did not enter a number dumbass.")

# Exempel personnummer

while True:
    personnummer = input("Enter your personal number YYMMDD-XXXX")

    if personnummer[:6].isdigit() and personnummer[-4:].isdigit() and len(personnummer) == 11 and personnummer[6] == "-":
        print("Thank you for entering your personalnumber correctly.")
        break
    else:
        print("dumbass")

    