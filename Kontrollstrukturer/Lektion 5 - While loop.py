# While True
"""
tries = 0
while True:
    tal = int(input("Skriv ett tal: "))
    tries += 1

    if tal == 27:
        print("Sant")
        break

    if tries == 3:
        print("Out of tries")
        break


# While condition
tries = 0
tal = None

while tries < 3 and tal != 27:
    tal = int(input("Skriv ett tal: "))
    tries += 1


# Continue
i = 0
while i < 100:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
    """
# Login

username = "Oskar_1337"
password = "Banan"
tries = 0
logged_in = False

while tries < 3:
    user1 = input("Username: ")
    pass1 = input("Password: ")

    if user1 == username and pass1==password:
        print("Logged in")
        logged_in = True
        break

    print("Wrong username or password\n")
    tries += 1

if logged_in == True:
    print("Secret information.")