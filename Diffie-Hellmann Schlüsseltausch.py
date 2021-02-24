def schluesseltausch(a, b, p, g):
    # Öffentliche Schlüssel
    alice_A = (g ** a) % p
    bob_B = (g ** b) % p
    print("Öffentlicher Schlüssel von Alice: \tA = (g^a) mod p = ({}^{}) mod {} = ".format(g, a, p) + str(alice_A))
    print("Öffentlicher Schlüssel von Bob: \tA = (g^a) mod p = ({}^{}) mod {} = ".format(g, b, p) + str(bob_B))

    # Geheimer Sitzungsschlüssel
    alice_K = (bob_B ** a) % p
    bob_K = (alice_A ** b) % p
    print("{0}{1}".format(
        "Von Alice berechneter geheimer Sitzungsschlüssel: \tK(Alice) = (B^a) mod p = ({}^{}) mod {} = ".format(bob_B,
                                                                                                                a, p),
        str(alice_K)))
    print("{0}{1}".format(
        "Von Bob berechneter geheimer Sitzungsschlüssel: \tK(Bob) = (A^b) mod p = ({}^{}) mod {} = ".format(alice_A, b,
                                                                                                            p),
        str(bob_K)))

    # Überprüfen auf Richtigkeit
    print("Überprüfung: K(Alice) = K(Bob)\t<=>\t {} = {}\t<=>\t {}".format(alice_K, bob_K, alice_K == bob_K))

    return


# Zahlen hier ändern
privkey_a = 4  # Privater Schlüssel von Alice
privkey_b = 6  # Privater Schlüssel von Bob
prime = 17  # öffentlich bekannte Primzahl
number = 3  # öffentlich bekannte natürliche Zahl, kleiner als p

# Output: Berechnet die öffentlichen Schlüssel und das Geheimnis von Alice und Bob
# Überprüft das Geheimnis auf Richtigkeit
schluesseltausch(privkey_a, privkey_b, prime, number)
