def monosub_dec(text, cipher_alphabet):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Konstruiere Disctionary mithilfe des gewählten "Cipher"-Alphabets
    dictionary = dict()
    for i in range(26):
        dictionary[cipher_alphabet[i]] = alphabet[i]

    result = ""
    # Entschlüsselung durch das Dictionary
    for i in range(len(text)):
        char = dictionary[text[i]]
        result += char
    return result


# Text und kryptographisches Alphabet hier ändern
cipher = "dovjrtjroz"
ciph_alph = "snvfrghjoklaympqwtdzibecxu"

# Output
print("Alphabet: \t\t\t" + "abcdefghijklmnopqrstuvwxyz")
print("Krypt. Alphabet: \t" + ciph_alph)
print("Cipher: \t\t\t" + cipher)
print("Klartext: \t\t\t" + monosub_dec(cipher, ciph_alph))
