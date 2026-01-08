name = input("Name: ")

while True:
    score = 0
    difficulty = input("Easy, hard or quit? ").lower()

    if difficulty == "easy":
        print("Welcome to the easy quiz.")
        ans1 = input("What is the capital of England? ").lower()
        if ans1 == "london":
            print("Correct")
            score += 1

        else:
            print("Incorrect")

        print(f"Quiz over, you got {score} points.")


    elif difficulty == "hard":
        print("Welcome to the hard quiz.")
        ans1 = input("Whats the meaning of life? ").lower()
        if ans1 == "42":
            print("Correct")
            score += 1

        else:
            print("Incorrect")

        print(f"Quiz over, you got {score} points.")

    elif difficulty == "quit":
        break

    else:
        print("Not a valid option")


