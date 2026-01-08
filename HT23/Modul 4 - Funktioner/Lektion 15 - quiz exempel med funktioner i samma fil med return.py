def easy_quiz() -> int:
    score = 0
    print("Welcome to the easy quiz.")
    ans1 = input("What is the capital of England? ").lower()
    if ans1 == "london":
        print("Correct")
        score += 1

    else:
        print("Incorrect")
    return score
    

def hard_quiz() -> int:
    score = 0
    print("Welcome to the hard quiz.")
    ans1 = input("Whats the meaning of life? ").lower()
    if ans1 == "42":
        print("Correct")
        score += 2

    else:
        print("Incorrect")

    return score

    
name = input("Name: ")
score = 0
while True:
    
    difficulty = input("Easy, hard or quit? ").lower()

    if difficulty == "easy":
        score += easy_quiz()

    elif difficulty == "hard":
        score +=  hard_quiz()

    elif difficulty == "quit":
        print(f"Quiz over, you got {score} points.")
        break

    else:
        print("Not a valid option")


