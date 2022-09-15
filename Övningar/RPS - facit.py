# Basic - 9 if
import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ")

print("The computer chose", computer,"and the user chose", user +".")

# TODO - Implement the if statements that prints who wins

if user == "rock" and computer == "paper":
    print("computer wins")

elif user == "paper" and computer == "scissors":
    print("computer wins")

elif user == "rock" and computer == "scissors":
    print("user wins")

elif user == "paper" and computer == "rock":
    print("user wins")

elif user == "rock" and computer == "rock":
    print("tie ")

elif computer == "scissors" and user == "paper":
    print("computer wins")

elif computer == "paper" and user == "paper":
    print("tie")

elif computer == "paper" and user == "scissors":
    print("user wins")

elif user == "scrissors" and computer == "scissors":
    print("tie ")

# Lika med => tie - 7 if

import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ")

print("The computer chose", computer,"and the user chose", user +".")
if user==computer:
    print("Draw play again.")
elif computer == ("rock") and user == ("paper"):
    print("user wins")
elif computer ==("paper") and user == ("scissors"):
    print("user wins")
elif computer ==("scissors") and user ==("rock"):
    print("user wins")
elif user == ("rock") and computer == ("paper"):
    print("big L")
elif user ==("paper") and computer == ("scissors"):
    print("Big L")
elif user ==("scissors") and computer ==("rock"):
    print("Big L")

# Lika som ovan fast med and
import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ")

print("The computer chose", computer,"and the user chose", user +".")

# TODO - Implement the if statements that prints who wins

if computer == "rock" and user == "scissors" or computer == "paper" and user == "rock" or computer == "scissors" and user == "paper":
    print("Computer wins!")
elif computer == "scissors" and user == "rock" or computer == "rock" and user == "paper" or computer == "paper" and user == "scissors":
    print("User wins!")
else:
    print("Draw!")

# 5 if
import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ")

print("The computer chose", computer,"and the user chose", user +".")

# TODO - Implement the if statements that prints who wins

if user == "rock" and computer == "scissors": 
    print ("Win")


elif user == "paper" and computer == "rock": 
    print ("Win")


elif user == "scissors" and computer == "paper": 
    print ("Win")


elif user == computer:
    print ("draw")

else:
    print("lose")



# Sista elevlösningen
import random

while True:

    computer = random.choice(["rock", "paper", "scissors"])

    user = input("rock, paper or scissors?\n")


    while True:
        
        if user == computer:
            print(f"You took {user} and the computer took {computer} so it is a draw you suck bozo ")

        elif user == "rock":
            if computer == "scissors":
                print("You won!")
                
            else:
                print("You lost!")
               
        elif user == "scissors":
            if computer == "paper":
                print("You won!")
                
            else:
                print("You lost!")
                

        elif user == "paper":
            if computer == "rock":
                print("You won!")
                
            else:
                print("You lost!")
                

        break

# Index - 3 if
import random

possible_choices = ["rock", "paper", "scissors", "fire", "lizard"]

computer = random.choice(possible_choices)

user = input("rock, paper, scissors, fire or lizard? ")

print("The computer chose", computer,"and the user chose", user +".")

# TODO - Implement the if statements that prints who wins
if possible_choices.index(user) - possible_choices.index(computer) == 1:
    print("User wins")

elif possible_choices.index(user) - possible_choices.index(computer) in  [-1, len(possible_choices)-1]:
    print("Computer wins")

else:
    print("Tie")
