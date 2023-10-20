"""
E
Eleven anpassar med viss säkerhet sin planering av programmeringsuppgiften
 och utför felsökning 
 av enkla syntaxfel.

C
Eleven anpassar med viss säkerhet sin planering av programmeringsuppgiften
och utför på ett systematiskt sätt felsökning 
av syntaxfel, körtidsfel och programmeringslogiska fel.

A
Eleven anpassar med säkerhet sin planering av programmeringsuppgiften 
och utför på ett systematiskt och effektivt sätt felsökning 
av syntaxfel, körtidsfel och programmeringslogiska fel.
"""

# SYNTAXFEL - Går att se innan koden körs

# SyntaxError
print("Hello, world!)
      

# KÖRTIDSFEL - Går att se när koden körs

# TypeError
print("5" + 5)

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





# PROGRAMMERINGSLOGISKA FEL

# Logisk error i en formel
# Beräknar arean av en cirkel med fel formel
radius = 5
area = 2 * 3.14 * radius  # Borde vara 3.14 * radius * radius


# Använder fel variabel i en beräkning
num1 = 10
num2 = 5
result = num1 - num1  # Borde vara num1 - num2

# Logisk error i en loop
# Felaktig range
i = 0
while i > 0:  # Borde vara i < 10
    print(i)
    i += 1

# Logisk error i matematiken
x = 5
y = 2
result = x + y ** 2  # Borde vara (x + y) ** 2







