# While-loop - exempel från tidigare
"""
password = "ja"
tries = 0
logged_in = False
while True:
    login = input("Vad är lösenordet? ")
    if login == password:
        print("Successfully logged in")
        logged_in = True
        break
    else:
        print("Try again")
        tries += 1
    
    if tries == 3:
        print("You tried 3 times, no log in for you.")
        break

if logged_in == True:
    print("Här är du inloggad.....")
"""



# isdigit
age = input("Skriv in din ålder: ")
while True:

    if age.isdigit():
        age = int(age)
        break
    else:
        age = input("Du måste skriva ett tal. \nSkriv in din ålder: ")

# Walrus
password = "ja"
login = input("Vad är lösenordet? ")

while login != password:
    login = input("Fel lösenord, vad är lösenordet? ")
    
password = "ja"

while login := input("Vad är lösenordet? ") != password:
    print("Fel lösenord")






# Walrus - isdigit()
while not (age := input("How old are you?")).isdigit():
    print("Please enter a number")

age = int(age)