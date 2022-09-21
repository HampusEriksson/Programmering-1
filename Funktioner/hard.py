def hard_quiz():
    score = 0
    print("Welcome to the hard quiz.")
    ans1 = input("Whats the meaning of life? ").lower()
    if ans1 == "42":
        print("Correct")
        score += 1

    else:
        print("Incorrect")

    print(f"Quiz over, you got {score} points.")