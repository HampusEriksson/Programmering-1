score = 0

ögon = input("vilken färg är dina ögon?").capitalize()
if ögon == ("Brun"):
    print ("helt rätt")
    score +=5
else: print("tyvärr fel")

huvudstad = input("vad är sveriges huvudstad?").capitalize()
if huvudstad == ("Stockholm"):
    print ("helt rätt")
    score +=5
else: print("tyvärr fel")

gymnasiet = input("vilket gymnasiet går du?").capitalize()
if gymnasiet == ("Nti"):
    print ("helt rätt")
    score +=5
else: print("tyvärr fel")

mat = input("vad är din favorit mat?").capitalize()
if mat == ("Pizza"):
    print ("helt rätt")
    score +=5
else: print("tyvärr fel.")

poäng = input("vill du se dina poäng?").capitalize()
if poäng == ("Ja"):
    
    print ("Hej", score)