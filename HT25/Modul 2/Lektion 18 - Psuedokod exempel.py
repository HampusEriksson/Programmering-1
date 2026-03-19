# Ta in nummer från användaren
tal = int(input("Skriv ett tal: "))
# Om talet är mindre än 1, skriv ut "inte primtal" och avsluta programmet
if tal < 1:
    print("Inte primtal")
# Om talet är 1 eller 2, skriv ut "primtal" och avsluta programmet
elif tal == 1 or tal == 2:
    print("Primtal")
# Om talet är större än 2, kolla om det är jämnt delbart med något tal mellan 2 och talet-1
elif tal > 2:
    for i in range(2, tal):
        if tal % i == 0:
            print("Inte ett primtal")
            break
    # Else kopplat till en for körs endast då for-loopen INTE blev breakad
    else:
        print("Primtal")

# Så fort vi hittar ett tal som är delbart med talet, skriv ut "inte primtal" och avsluta programmet

# Om vi inte hittar något tal som är delbart med talet, skriv ut "primtal" och avsluta programmet


