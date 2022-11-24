
# En tom lista skapas för att kunna hantera en travelbag
travelbag = []

# Programmet visar en meny med val. Skapar en loop som kommer köras tills användaren trycker 4.
while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program\n")

# Om användaren trycker 1 så printas/skrivs innehållet i listan travelbag ut
   if menyval == "1":
       print(*travelbag)

# Om användaren trycker 2 så kan användaren lägga till något i listan travelbag med input
   elif menyval == "2":
       ny_sak = input("Lägg till något:")
       travelbag.append(ny_sak)

# Om användaren trycker 3 så kan användaren ta bort något i listan travelbag med input
   elif menyval == "3":
       tabort = input("Ta bort:")
       travelbag.remove(tabort)

   elif menyval == "4":
       break