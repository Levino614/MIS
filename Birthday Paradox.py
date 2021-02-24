def birthdayparadox(p, g):
    # Paare an Personen mit potentiell selbem Geburtstag
    x = p * (p-1) / 2

    # Wahrscheinlichkeit, dass zwei Personen einen unterschiedlichen Geburtstag haben
    pz = (g-1)/g

    # Wahrscheinlichkeit, dass alle Personen einen unterschiedlichen Geburtstag haben
    pa = pz ** x

    # Wahrscheinlichkeit, dass zwei beliebige Personen DEN SELBEN Geburtstag haben (Kollision)
    return 1 - pa


# Anzahl der möglichen Personen und Geburtstage hier ändern
personen = 23
geburtstage = 365

# Output
print(birthdayparadox(23, 365))
