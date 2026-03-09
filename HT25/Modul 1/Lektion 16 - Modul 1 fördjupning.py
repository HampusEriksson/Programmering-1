# Print
print("Välkommen till programmet!")

# Print - format
namn = "Hampus"
print(f"Välkommen till programmet {namn}!")

# Print, med ,
print("Välkommen till programmet", namn, "!")

# Print - sep och end
print("Adam", "Aydarus", "Olof", "Ahmet", "Nuur", sep=" - ", end=".\n")

# Print - ny rad
print("Natanael\nAlper\nFeisel\nRebecka")

# Print - tab emellan
print("Natanael\tAlper\tFeisel\tRebecka")

# Print - citattecken
print('"min text"')
print("'min text'")
# Print - multi-line
print("""Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
      Repudiandae non iste sint, rerum quisquam iure, 
      soluta nulla commodi omnis similique veniam? 
       """)
# Kommentarer - förklarar programmet
# Körs inte när programmet körs
print("Denna körs när programmet körs")

# 3 citattecken är multiline kommentar
"""Här är en multiline
kommentar.
"""

# Input - str som default
# String - text
username = input("Enter your username\n")

# Int - input
# Heltal - int
age = int(input("Enter your age\n"))

# Decimaltal - float
grade = float(input("Enter your gradescore\n"))

# Paus med input
input("Press enter to continue...")