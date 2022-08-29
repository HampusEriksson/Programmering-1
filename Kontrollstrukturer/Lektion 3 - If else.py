# Booleans
# En datatyp
# 2 möjliga värden
True
False
"""
print(5 < 7)

age = int(input("How old are you?"))

# if
if age >= 69:
    print("You are retired, nice.")

# elif
elif age >= 50:
    print("Half way down ish.")

elif age >= 18:
    print("You are an adult, at least on paper.")

# else
else:
    print("Grow up!")



# .lower, .upper, .capitalize
name = input("What is your name?").capitalize()

# or - exempel 1
if name == "Alex" or name == "Oskar" or name == "Hampus":
    print("You are my favorite")

else:
    print("Go away please.")

# or - exempel 2
if name in ["Alex", "Oskar", "Hampus", "Hanna"]:
    print("You are my favorite")

else:
    print("Go away please.")
"""

# and

username = input("Username: ")
password = input("Password: ")

if username == "hampuse1" and password == "Hampus123":
    print("You are logged in.")

else:
    print("Username or password is incorrect.")