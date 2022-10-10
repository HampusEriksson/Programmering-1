score =0
fot = input ("vilket lag hejar Mohammed?").capitalize
if fot == ("real madrid"):
    print ("rätt som fan")
    score +=3
else: 
    print ("tyvärr fel")

spelare = input ("vem är världens bästa spelare enligt mohammed?").capitalize
if spelare == ("Benzema"):
    score +=3
    print ("korrekt")
else: 
    print ("tyvärr fel")

Elit = input("Hur många Ballon d'Or har ronaldo vunnit?").capitalize
if Elit == ("5"):
    print ("korrekt")
    score +=3
else: print ("tyvärr fel")

mål = input("hur många mål har Benzema gjort under 2021/2022 säsongen?")
if mål == ("100 mål"):
    print ("helt rätt")
    score +=3

else: print ("tyvärr fel")