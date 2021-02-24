# Verschlüsselt Message M mithilfe des öffentlichen Schlüssels (e, N)
def RSA_enc(M, e, N):
    C = (M ** e) % N
    print("C = (M^e) mod N = ({}^{}) mod {} = {}".format(M, e, N, C))
    return C


# Zufällig gewählte und stochastisch unabhängige Primzahlen p und q hier ändern
prime1 = 3
prime2 = 13

# Zu verschlüsselnde Nachricht und öffentlichen Schlüssel hier ändern
text = 10
pub_key = 23

print("-------Nachricht verschlüsseln-------")
RSA_enc(text, pub_key, prime1*prime2)
