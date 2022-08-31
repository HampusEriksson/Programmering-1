# Hur ändrar man en variabel
score = 0

# Lägg till 3 på två olika sätt
score += 3
score = score + 3

# Ta bort 5 på två olika sätt
score -= 5
score = score - 5

answer1 = input("Vem är Ashs första Pokemon?")

print("A. Paris\nB. Budapest\nC. London")
answer2 = input("Vilken är Frankrikes huvudstad?")

print("Vilken är Sveriges huvudstad?")
answer3 = input().capitalize()

if answer3 == "Stockholm":
    score += 3