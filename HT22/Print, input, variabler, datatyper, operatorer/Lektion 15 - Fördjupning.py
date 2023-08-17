"""
# Print
print("Hampus förtjänar en löneförhöjning")
name = "Hampus"

print(name, "förtjänar en löneförhöjning")

# Två parametrar - sep och end - kan förändra utskrift
print(name, "förtjänar en löneförhöjning", sep = " ", end="\n")

# Format
print(f"{name} förtjänar en löneförhöjning")
"""
# Citattecken
print("Hampus 'förtjänar' en löneförhöjning")
print('Hampus "förtjänar" en löneförhöjning')

# Multi-line str
message = """Hej på dig.
Välkommen till mitt spel.
Lycka till."""
print(message)

# Ny rad i str
message = "Hej\npå\ndig"
print(message)

# Input
name = input("Vad heter du? ")
print(name)

# Int - input
age = int(input("Hur gammal är du? "))

# Variabel

# String - text
"Här är en text"

# Heltal - int
69

# Decimaltal - float
69.420

# Kommentarer - förklarar programmet

# Användaren skriver in sin ålder med input och konverterar till int. Sparas i age
age = int(input("Hur gammal är du? "))

# 3 citattecken är multiline kommentar

"""Kommentar
Kommentar
Kommentar"""