# While-loop
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

# Walrus



while True:
    height = input("Write your height: ")

    if not height.isdigit():
        continue

    else:
        height = int(height)
        break

if height < 170:
    print("Lol you are short")
    
else:
    print("Wow so tall lamppost")
    


# Walrus - isdigit()



while not (height := input("Write your height: ")).isdigit() :
    print("Please enter a number\n")

height = int(height)

if height < 170:
    print("Lol you are short")
        
else:
    print("Wow so tall lamppost")
    

while  not (pers_nr := input("Enter your social security number: ")).isdigit() or len(pers_nr) != 10:
    print("Please enter in the form of YYMMDDXXXX")


# While else

# Nästlade while-loopar