# Booleans
# En datatyp
# 2 möjliga värden
True
False

# Skriva ut boolean 
print(5 > 7)

age = int(input("How old are you?"))

# if else - kontrollstruktur
if (age < 12):
    print("Du har långt kvar till bilen")
elif (age < 18):
    print("Du får inte köra bil.")
elif (age >= 75):
    print("Du är för gammal.")
else:
    print("Du får övningsköra.")

# .lower() (små bokstäver), .upper() (stora bokstäver)
# .capitalize() (första bokstaven stor, resten små)
# or
glass = input("Vill du ha glass?")
glass = glass.capitalize()

if (glass == "Ja") or (glass =="Yes"):
    print("Här får du glass.")
else:
    print("Du får inte glass.")



# and


