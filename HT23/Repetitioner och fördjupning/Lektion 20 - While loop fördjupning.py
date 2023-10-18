# While-loop - exempel från förra året
"""
username = "Oskar_1337"
password = "Banan"
tries = 0
logged_in = False #Boolean - bool

while tries < 3:
    user1 = input("Username:  ")
    pass1 = input("Password: ")

    if user1 == username and pass1==password:
        print("Logged in")
        logged_in = True
        break
    else:
        print("Wrong username or password\n")
        tries += 1

if logged_in == True:
    print("Secret information.")
"""




# isdigit
while True:
    age = input("How old are you? ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Please enter a number")

# Walrus - isdigit()
while not (age := input("How old are you?")).isdigit():
    print("Please enter a number")

age = int(age)

# Walrus
while  (date := input("Enter a date with format DDMMYYYY\n")).isdigit() == False or len(date) != 8:
    print("Wrong inputed date.") 