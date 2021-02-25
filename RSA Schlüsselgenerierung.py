# Hilfsfunktion größter gemeinsamer Teiler
def ggT(a, b):
    if b == 0:
        return a
    else:
        return ggT(b, a % b)


# Generiert die Schlüssel
def RSA_genkey(p, q):
    # Berechne das RSA-Modul N aus den Primzahlen p und q
    N = p * q
    print("N = p * q = {} * {} = {}".format(p, q, N))

    # Berechne die Eulersche phi-Funktion von N
    phi = (p-1) * (q-1)
    print("phi = (p-1) * (q-1) = ({}-1) * ({}-1) = {}".format(p, q, phi))

    # Wähle eine zu phi teilerfremde Zahl e
    e = phi
    while ggT(phi, e) != 1:
        e = int(input("Wähle eine zu phi = {} teilerfremde Zahl e = ".format(phi)))

    # Berechne den Entschlüsslungsexponenten d als multiplikativ Inverses von e bezüglich des Moduls phi(N):
    # e*d mod phi(N) = 1

    # Hier zu aufwändig

    print("Privater Schlüssel: d und N = {}".format(N))
    print("Öffentlicher Schlüssel: e = {} und N = {}".format(e, N))
    print("Idee: d lässt sich nur dann berechnen, wenn man p und q kennt. Die Zerlegung von N in p und q ist nur "
          "mit sehr hohem Aufwand möglich.")
    return e


# Zufällig gewählte und stochastisch unabhängige Primzahlen p und q hier ändern
prime1 = 3
prime2 = 13

# Output
print("---------Schlüssel generieren---------")
RSA_genkey(prime1, prime2)
