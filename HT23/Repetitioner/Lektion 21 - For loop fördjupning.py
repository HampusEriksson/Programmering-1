import random
students = ["Batin", "Alec", "Yassin", "Diana", "Lion", "Hundaol", "Rasmus", "Lucia", "Robert", "Isak"]


# For-loop
for _ in range(10):
    print("Hej")

# Loop-variabel
for i in range(10): # (start = 0, stop = 10, step = 1)
    print(i)

# start, stop, step
for i in range(100,9,-2):
    print(i)


# Loopa lista

for student in students:
    print(student)

for index, student in enumerate(students):
    if random.random() <= 0.2:
        print(f"{student} got kicked from the class. Impostor replaces.")
        students[index] = "Impostor"
    else:
        print(f"{student} gets to stay in the class.")
    input()


# For else
for index, student in enumerate(students):
    if random.random() <= 0.01:
        print(f"{student} got kicked from the class. Impostor replaces.")
        students[index] = "Impostor"
        break
    else:
        print(f"{student} gets to stay in the class.")

# else körs om break inte körts i for-loop ovan
else:
    print("Noone got kicked from the class.")

# Nästlade for-loopar
enemy_pos = [(random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100))]
bullet_pos = [(random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100))]

for enemy in enemy_pos:
    for bullet in bullet_pos:
        if ((enemy[0] - bullet[0])**2 + (enemy[1] - bullet[1])**2)**0.5 <= 5:
            print("It's a hit")
            