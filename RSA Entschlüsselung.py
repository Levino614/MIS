# Entschlüsselt Ciphertext C mithilfe des Entschlüsslungsexponenten d und N
# Zusammen ergeben diese den privaten Schlüssel (d, N)
def RSA_dec(C, d, N):
    M = (C ** d) % N
    print("M = (C^d) mod N = ({}^{}) mod {} = {}".format(C, d, N, M))
    return M


# Zufällig gewählte und stochastisch unabhängige Primzahlen p und q hier ändern
prime1 = 3
prime2 = 13

# Verschlüsselte Nachricht und privaten Schlüssel d hier ändern (aus Aufgabe gegeben)
cipher = 4  # Verschlüsselte Nachricht
priv_key = 5     # privater Schlüssel d

# -------Nachricht entschlüsseln-------
RSA_dec(cipher, priv_key, prime1*prime2)
