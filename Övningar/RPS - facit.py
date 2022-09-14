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
