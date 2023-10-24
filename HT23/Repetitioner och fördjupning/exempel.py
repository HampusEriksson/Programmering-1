a = int(input("Ange ett tal: "))
b = int(input("Ange ett tal: "))

try:
    print(a/b)

except ZeroDivisionError:
    print("Du kan inte dela med 0!")

except ValueError:
    print("Du måste ange ett tal!")

except:
    print("Något gick fel!")