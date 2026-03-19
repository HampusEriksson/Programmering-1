for tal in range(100):
    ord = ""
    if tal % 3 == 0:
        ord += "Fizz"
    if tal % 5 == 0:
        ord += "Buzz"
    if tal % 7 == 0:
        ord += "Cazz"
    if ord == "":
        print(tal)
    else:
        print(ord)