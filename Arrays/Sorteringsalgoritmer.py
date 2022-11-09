tal = [2,5,1,7,8,0, 3]

# Byt plats på index 0 och index 2
tal[0], tal[2] = tal[2], tal[0]

# Dela upp listan i mindre delar
half = int(len(tal)/2)
del1 = tal[:half]
del2 = tal[half:]

print(tal1, tal2)