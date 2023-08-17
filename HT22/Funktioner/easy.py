def easy_quiz():
    score = 0
    print("Welcome to the easy quiz.")
    ans1 = input("What is the capital of England? ").lower()
    if ans1 == "london":
        print("Correct")
        score += 1

    else:
        print("Incorrect")

    print(f"Quiz over, you got {score} points.")