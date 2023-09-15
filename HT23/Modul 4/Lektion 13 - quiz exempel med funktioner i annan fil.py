# Importera funktionen easy_quiz från filen easy.py
from easy import easy_quiz
from hard import hard_quiz

name = input("Name: ")

while True:
    
    difficulty = input("Easy, hard or quit? ").lower()

    if difficulty == "easy":
        easy_quiz()
        
    elif difficulty == "hard":
        hard_quiz()

    elif difficulty == "quit":
        break

    else:
        print("Not a valid option")


