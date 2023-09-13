# i = loopvariabel
for ok in range(10, 23, 3):
    print(ok**2)
tries = 0
while True:
    namn = input("Vad heter du? ")
    if namn == "Alex":
        print("Hej Alex!")
        break
    else:
        print("Hej", namn, "!")
        tries += 1
    
    if tries == 3:
        print("Du har försökt för många gånger!")
        break
        

tries = 0
while tries < 3:
    namn = input("Vad heter du? ")
    if namn == "Alex":
        print("Hej Alex!")
        
    else:
        print("Hej", namn, "!")
        tries += 5
        

print("Här är vi ute från while loopen!")