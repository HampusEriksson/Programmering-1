"""
Print
Input
Variabler
Datatyper
Konvertering
Operatorer
"""

# Variabler
# variabelnamn = värde

namn = "Adam"

# String - text - citattecken runt - "adam"

print(namn)

ålder = 17

# Integer - heltal - utan citattecken - 17

print(f"Personen heter {namn} och är {ålder} år gammal.")

# input
# variabel = input("Din fråga: ")
username = input("Ange ditt namn: ")
age = int(input("Ange din ålder: "))

print(f"Du heter {username} och är {age} år gammal.")

# float - decimaltal
temp = 7.7

# operatorer
a = 10
b = 3

print(a + b) # addition
print(a - b) # subtraktion
print(a * b) # multiplikation
print(a / b) # division
print(a // b) # heltalsdivision
print(a ** b) # upphöjt
print(a % b) # modulus - ger resten vid division
