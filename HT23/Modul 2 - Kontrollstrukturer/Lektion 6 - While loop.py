# While True
secret_word = "gustav vasa"
while True:
    svar = input("Vem vill du kyssa?")
    if svar == secret_word:
        break
    else:
        print("Wrong")
    

# While condition
svar =""
while svar != secret_word:
    svar = input("Vem vill du kyssa?")

# Login
user = "hampus1"
password = "hej123"

user_input = input("What is your username?")
user_password = input("What is your password?")

while user != user_input and password != user_password:
    print("Password or username is incorrect.")

    user_input = input("What is your username?")
    user_password = input("What is your password?")



# Continue
# continue can help streamline code and avoid 
# unnecessary processing when certain conditions are met.
count = 0

while count < 5:
    count += 1
    
    if count == 3:
        print("Skipping iteration", count)
        continue
    
    print("Iteration", count)

print("Loop finished")

