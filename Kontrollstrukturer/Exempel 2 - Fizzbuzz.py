# Fizz buzz exempel
"""Gör ett program som skriver ut alla tal mellan 0 och 100.
Lägg till kod så att programmet skriver ”Fizz” istället för talet om det är delbart med 3.
Lägg till kod så att programmet skriver ”Buzz” istället för talet om det är delbart med 5.
Gör så att programmet skriver ”FizzBuzz” om det är delbart med 3 och 5. 
Tillagt efter FizzBuzz
Lägg till kod så att programmet skriver ”Cazz” istället för talet om det är delbart med 7.

"""
# FizzBuzzCazz lösning 2
for i in range(1,69):
    word = ""
    word += "Fizz" if i % 3 == 0 else ""
    word += "Buzz" if i % 5 == 0 else ""
    word += "Cazz" if i % 7 == 0 else ""

    print(word if word != "" else i)
    
"""
# FizzBuzz lösning 1
for i in range(1,69):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""