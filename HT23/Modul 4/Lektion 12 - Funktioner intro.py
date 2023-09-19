# Genomgång HT21: https://www.youtube.com/watch?v=wBtXipziN50&ab_channel=HampusEriksson

# Skapa en funktion
def my_function():
    print("Hello from a function")

# Anropa en funktion
my_function()

# Varför - exempel - print_score
def print_score(score):
    print(f"Your score is {score}, good job!")

print("Hello")
player1_score = 10
print_score(player1_score)
player1_score += 15
print_score(player1_score)
player1_score += 15
print_score(player1_score)
player1_score += 15
print_score(player1_score)
player1_score += 15
print_score(player1_score)
player1_score += 15
print_score(player1_score)

# Parametrar - exempel
# f(x)
# Returnera
def f(x):
    y = x**2 + 2*x
    return y

my_x = 10
my_y = f(my_x)
print(my_y)


# Default värden - raised
def raised(x :int, y=2) -> int:
    return x**y

print(raised(5))

# Returnera flera värden
# En tuple returneras
def raised(x, y=2) -> tuple:
    return x**y, y**x

print(type(raised(5)))