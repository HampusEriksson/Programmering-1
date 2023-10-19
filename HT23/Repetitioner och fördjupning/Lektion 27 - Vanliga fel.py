# TypeError
print("5" + 5)

# SyntaxError
print("Hello, world!)

# NameError
print(variable_that_does_not_exist)

# IndexError
my_list = [1, 2, 3]
print(my_list[3])

# ValueError
int("hello")

# AttributeError
my_list = [1, 2, 3]
my_list.append(4, 5)

# KeyError
my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict["key3"])

# ZeroDivisionError
print(1/0)

# IndentationError
def my_function():
print("Hello, world!")

"""
Eleven anpassar med säkerhet sin planering av programmeringsuppgiften 
och utför på ett systematiskt och effektivt sätt felsökning 
av syntaxfel, körtidsfel och programmeringslogiska fel.
"""

# Syntaxfel - Går att se innan koden körs

# Körtidsfel - Går att se när koden körs

# Programmeringslogiska fel

# Logical error in a formula
# Calculating the area of a circle incorrectly
radius = 5
area = 2 * 3.14 * radius  # Should be 3.14 * radius * radius


# Using the wrong variable in a calculation
num1 = 10
num2 = 5
result = num1 - num1  # Should be num1 - num2

# Logical error in a loop termination condition
# This loop will run infinitely
i = 0
while i > 0:  # Should be while i < 10
    print(i)
    i += 1

# Logical error in the order of operations
x = 5
y = 2
result = x + y * 2  # Should be (x + y) * 2

# Logical error related to indexing
# Iterating through a list with an incorrect range
my_list = [1, 2, 3, 4, 5]
for i in range(5):  # Should be range(len(my_list))
    print(my_list[i])






