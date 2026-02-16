# Skapa/definerar en funktion
def welcome():
    print("Welcome to the program, happy to see you here.")

# Anropa en funktion
welcome()
welcome()
welcome()

# Varför - exempel - print_score
def print_score(score):
    print(f"You have {score} points, good job!")

my_score = 136
print_score(my_score)
print_score(783)
# Parametrar - exempel
# f(x)
# Returnera

def f(x : int) -> int:
    return x**2 + 2*x + 3

y = f(2)
adams_tal = f(8)
print(adams_tal)
print(f"Adams tal blev {adams_tal}")

# age-checker
def age_checker(age):
    if age >=18:
        return True
    else:
        return False

my_age = int(input("What is your age? "))
if age_checker(my_age) == True:
    print("Du är myndig")
else:
    print("Du är inte myndig")


# Default värden - raised
def raised(x, y = 2):
    print(x ** y)

raised(3,3)
raised(2)
raised(97, 189)

