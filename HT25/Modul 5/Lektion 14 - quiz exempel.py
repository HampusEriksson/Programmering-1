def easy_quiz():
    score = 0

    svar = int(input("Vad är 1+1?"))
    if svar == 2:
        score += 1
        print("Rätt svar")
    else:
        print("Fel svar")
    
    svar = input("Vad är 3+5?")
    if svar == "8":
        score += 1
        print("Rätt svar")
    else:
        print("Fel svar")

    print(f"Du fick {score} poäng")

def hard_quiz():
    score = 0

    svar = int(input("Vad är 89^198?"))
    if svar == 89**198:
        score += 1
        print("Rätt svar")
    else:
        print("Fel svar")
    
    svar = float(input("Vad är roten ur 2?"))
    if svar == 2**0.5:
        score += 1
        print("Rätt svar")
    else:
        print("Fel svar")

    print(f"Du fick {score} poäng")


while True:
    choice = input("1. Hard quiz\n2. Easy quiz \n3. Quit\n")
    if choice == "1":
        hard_quiz()
    elif choice == "2":
        easy_quiz()
    elif choice == "3":
        break
    else:
        print("Invalid choice")