# Booleans
# En datatyp
# 2 möjliga värden
True
False


print(5 < 7)

age = int(input("How old are you?"))

# if
if age < 18:
    print("You are not an adult.")
elif age > 100:
    print("You gonna die soon.")
elif age > 65:
    print("You are retired.")
# else
else:
    print("You are an adult between 18 and 65.")


mood = input("Mår du bra?").capitalize()

# .lower, .upper, .capitalize
if mood == "Ja" or mood == "Ja, väldigt bra":
    print("Vad härligt!")
else:
    print("Åh nej")


fruit = input("Name a fruit.").lower()
# or - exempel 1
if fruit == "apple" or fruit == "orange" or fruit == "pear" or fruit == "peach":
    print("Correct, thats a fruit.")

# or - exempel 2
fruits = ["apple", "orange", "peach", "pear"]
if fruit in fruits:
    print("Correct, thats a fruit.")

# and

username = input("Username: ")
password = input("Password: ")

if username == "hampuse1" and password == "Hampus123":
    print("You are logged in.")

else:
    print("Username or password is incorrect.")
