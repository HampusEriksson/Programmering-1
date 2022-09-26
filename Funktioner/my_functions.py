def pythagoras(a, b):
    """Räkna ut hypotenusan"""
    return (a**2 + b**2)**0.50

def comp_str(str1, str2):
    if str1.lower() == str2.lower():
        return True
    else:
        return False

# Denna funktion tar in p och q och returnerar två lösningar
def pq(p, q):
    under_rot = ((p/2)**2-q)**0.50

    return (-p/2 + under_rot, -p/2 - under_rot)
