import random

# Random integer
a = random.randint(1,50)
print(a)

# Random float - uniform
b = random.uniform(1,50)
print(b)

# Random between 0-1
c = random.random()
print(c)

# Slump med procent
if c > 0.9:
    print("You were very lucky.")

# Random letters
name = "sebastian vettel"

print(random.choice(name))

# Random choice
students = ["Diana", "Rasmus", "Alexander"]
print("Den som får A i programmering är: ", random.choice(students))
