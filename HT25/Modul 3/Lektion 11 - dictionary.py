
# Dåligt sätt
usernames = ["Hampus", "Shiva", "Mohannad"]
passwords = ["1234", "gazim67", "cere65LYN"]

# Users
# Skapa dictionary
# Key-value pair
users = {"Hampus" : "1234", "Shiva" : "gazim67", "Mohannad": "cere65LYN"}

print(users["Shiva"])
# Lägg till key-value pair
username = input("Register your username: ")
password = input("Register your password: ")

if username not in users.keys():
    users[username] = password
else:
    print("User already exist, enter your old password to change it.")
    old_password = input("Enter your old password: ")
    if old_password == users[username]:
        users[username] = password

# loopa igenom dictionary
for name in users.keys():
    print(name)

for lösen in users.values():
    print(lösen)

# Ta bort - del

# .keys()


# .values()


# .items()




# Räkna händelser
