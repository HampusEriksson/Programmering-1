# Tänk på från igår:
# Variabler med små bokstäver
name = "Hampus" # Rätt
Name = "Hampus" # Fel

# print och input görs med små bokstäver
print("NTI är bäst") # Rätt
# Print("NTI är bäst") # Fel, ger error


name = input("What is your name?\n")

# Input med heltal
# Bästa sättet
age = int(input("What is your age?"))

# Krångligare sätt, men inte fel
months = input("How many months til' your birthday?")
months = int(months)

print(age)
"29"
print(100-age)

my_number = 27
# Addition
my_number += 8

new_number = 100 + my_number

print(my_number)
print(new_number)

# Subtraktion
my_number -= 8

new_number = 100 - my_number

print(my_number)
print(new_number)

# Multiplikation
my_number *= 8

new_number = 100 * my_number

print(my_number)
print(new_number)

# Division
my_number /= 8

new_number = 100 / my_number

print(my_number)
print(new_number)

# Upphöjt i. ** betyder upphöjt i
squared_number = 5 ** 2

# Floor division - Hur många 5 får plats i 17?
print(17 // 5)


# Modulo - Hur stor rest kvar?
print(17 % 5)