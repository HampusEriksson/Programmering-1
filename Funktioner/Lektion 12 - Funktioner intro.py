# Förra årets genomgång: https://www.youtube.com/watch?v=wBtXipziN50&ab_channel=HampusEriksson

# Skapa en funktion
def hello_world():
    print("Hello world")

hello_world()

# Varför - exempel
def print_score(score):
    print(f"Din score är {score}.")

score = 500

print_score(score)

print_score(score)

print_score(score)

print_score(score)

print_score(score)

# Parametrar - exempel
# f(x)
# Returnera

def f(x):
    y = 2 * x + 4
    return y

mitt_tal = f(5)
print(mitt_tal)

# Default värden - raised

def raised(x, y = 2):
    return x ** y

print(raised(3, 3))

def min_funktion(name, age, nationality="Sweden"):
    print(name, age, nationality)

