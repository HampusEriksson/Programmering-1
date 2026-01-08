import random

# Random integer - randint(min, max)
a = random.randint(1,100)

# Random float - uniform(min, max)
b = random.uniform(1, 10)
print(b)

# Random between 0-1 - random.random()
c = random.random()
print(c)

# Slump med procent
if c < 0.1:
    print("Du dog, haha")
else:
    print("Du dog inte")

# Random letters - choice
namn = "Erik"

d = random.choice(namn)
print(d)

# Random from list - choice
students = ["Erik", "Vilgot", "Egli", "Gustav", "Vasa"]
e = random.choice(students)
print(e)
