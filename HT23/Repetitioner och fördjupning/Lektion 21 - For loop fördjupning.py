import random

# For-loop
for _ in range(10):
    print("Ni får prata om klippning sen.")

# Loop-variabel
for i in range(100):
    print(i)

# start, stop, step
for i in range(10, 115, 7):
    print(i)


students = ["Erik", "Vilgot", "Marcus", "Tom", "Daiki", "Egli"]
# Loopa lista
for student in students:
    print(student)

# Enumerate
for index, student in enumerate(students):
    if random.random() <=0.9:
        students[index] = "MARKUS"

print(students)

# For else
students = ["Erik", "Vilgot", "Marcus", "Tom", "Daiki", "Egli", "Mattias"]

for student in students:
    if student == "Mattias":
        break

else:
    print("For-loopen breakade inte")

for a in [1,2,3,4,5]:
    if a == 6:
        break

else:
    print("For-loopen breakade inte")

# Nästlade for-loopar
enemy_pos = [(random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100))]
bullet_pos = [(random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100)), (random.randint(1,100), random.randint(1,100))]

for enemy in enemy_pos:
    for bullet in bullet_pos:
        if ((enemy[0] - bullet[0])**2 + (enemy[1] - bullet[1])**2)**0.5 <= 5:
            print("It's a hit")
            