# Import my_functions

from my_functions import check_list


# https://www.w3schools.com/python/python_functions.asp
# Skapa funktion
def f(x):
    y = x * 3 + 70
    return y


def f2(x):
    y = x * 3 + 70
    print(y)


f15 = f(15)
print(f15)
print(f(127))

# Parametrar - det som skickas in till funktionen
# Datatyper på parametrar
# docstring


mobiler = ["iPhone 14", "One plus", "Blackberry", "Samsung 22"]

check_list(mobiler)
check_list("fiasgufoasgo")


def func(x, y):
    return x + y


print(func(5, 13))

# Lambda
# variabelnamn = lambda parameter1, parameter2 : returdata
func2 = lambda x, y: x + y

print(func2(5, 13))


# sortera list av tuples
students = [("Erik", 15), ("Adam", 17), ("Berit", 13), ("Carl", 20), ("David", 10)]

# Sorterar default på index [0]
students.sort()

# Om vi vill sortera på andra index, använd lambda-funktion
students.sort(key=lambda x: x[1])
print(students)
