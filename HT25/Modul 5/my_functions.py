import math
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

def pythagoras(a, b):
    # Räkna ut hypotenusans längd
    return math.sqrt(a**2 + b**2)

# Jämföra om två strängar är lika
def comp_str(str1, str2):
    if str1.lower() == str2.lower():
        return True
    else:
        return False

# Denna funktion tar in p och q och returnerar två lösningar
def pq(p, q):
    roten = math.sqrt((p/2)**2-q)

    return (-p/2 + roten, -p/2 - roten)

def check_list(stuff : list):
    """Check_list checks if the parameter is a list, and then runs .pop()"""
    if isinstance(stuff, list):
        stuff.pop()
        return stuff
    else:
        print("Parameters was not a list")
        return False