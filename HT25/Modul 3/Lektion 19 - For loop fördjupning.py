import random

# For-loop
for _ in range(100):
    print("Hej")

# Loop-variabel
# p får värderna 0 till 9
for p in range(10):
    print(p)

# start, stop, step
for r in range(13, 37, 2):
    print(r)
for x in range(100,0, -1):
    print(x)

# Loopa lista
students = ["Mohannad", "Rebecka", "Feisel"]

for student in students:
    print(student)

# Enumerate
for index,student in enumerate(students):
    print(f"{index+1} : {student}")
# For else
for student in students:
    if student == "Novak":
        print("Novak är här, wow!")
        break
else:
    # Det här körs endast då for-loopen INTE breakades
    print("Novak finns inte i klassen.")


