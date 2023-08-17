# Tidigare genomgång: https://www.youtube.com/watch?v=e3LL4mSrLMs&ab_channel=HampusEriksson

# Skapa dictionary
# Key-value pair
# Lägg till key-value pair - kolla först om den finns!
# Ändra value - kolla först om den finns!
# Ändra value med update - kolla först om den finns!
# Ta bort - del
# Ta bort - pop
# .keys()
# .values()
# .items()
grade_values = {"A":20, "B":17.5, "C":15,"D":12.5, "E":10, "F":0, "-":0}
grades = {"Teknik 1": "A", "Fysik 1" : "D"}
course_points = {"Teknik 1" : 150, "Fysik 1": 150, "Historia 1a": 50}

for x,y in grade_values.items():
    print(x,y)

while True:
    menyval = input("\n1. Kolla betyg\n"
                   "2. Ändra betyg\n"
                   "3. Lägg till betyg\n"
                   "4. Räkna ut meritvärde\n"
                   "5. Avsluta program\n")

    if menyval == "1":
        for course, grade in grades.items():
            print(f"{course} : {grade}")

    elif menyval == "2":
        course = input("Vilken kurs vill du ändra  ett betyg i? ").capitalize()
        if course in grades:
            grades[course] = input(f"Vilket betyg vill du ändra till i {course}? ").capitalize()
        else:
            print(f"Du har inte ett betyg i {course} just nu.")
            

    elif menyval == "3":
        course = input("Vilken kurs vill du lägga till ett betyg i? ").capitalize()
        if course in grades:
            print(f"Den kursen har redan ett betyg. {course} har betyget {grades[course]}.")

        else:
            grades[course] = input(f"Vilket betyg har du i {course}? ").capitalize()


    elif menyval == "4":
        poäng_total = 0
        kurs_total = 0
        for course, grade in grades.items():
            poäng_total += grade_values[grade] * course_points[course]
            kurs_total += course_points[course]

        print((poäng_total / kurs_total))
        if "-" in grades.values():
            print("Du har ett - i dina betyg. Du kan inte få gymnasieexamen.")

    elif menyval == "5":
        break
