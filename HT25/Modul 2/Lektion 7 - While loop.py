# While True
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

# While condition
password = "ja"
tries = 0
logged_in = False
login = ""
while (login != password) and tries < 3:
    
    login = input("Vad är lösenordet? ")
    tries += 1


if(login == password):
    logged_in = True

if logged_in == True:
    print("Här är du inloggad.....")



# Continue


