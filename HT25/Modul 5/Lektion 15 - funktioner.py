# Måste funktion ha return?
def welcome():
    print("Välkommen till programmet!")
    

def f(x):
    return x * 2

# None returneras
welcome()
# None är av datatypen NoneType
print(type(None))
print(welcome())
print(f(5))
print(f(13))



# Lokala och globala variabler

def lokal():
    # Lokal variabel namn, kan inte nås utanför funktionen
    namn = "Hampus"
    print("Lokalt test") 
lokal()

def add_score(addition):
    global score
    score += addition

score = 0
add_score(5)
print(score)

# Alternativ

def add_score2(score,addition):
    return score + addition

score = 0
score = add_score2(score, 5)
print(score)