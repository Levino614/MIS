def monosub_enc(text, cipher_alphabet):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Konstruiere Disctionary mithilfe des gewählten "Cipher"-Alphabets
    dictionary = dict()
    for i in range(26):
        dictionary[alphabet[i]] = cipher_alphabet[i]

    result = ""
    text = text.upper()
    # Verschlüsselung durch das Dictionary
    for i in range(len(text)):
        char = dictionary[text[i]]
        result += char
    return result


# Text und kryptographisches Alphabet hier ändern
input_text = "Sicherheit"
ciph_alph = "snvfrghjoklaympqwtdzibecxu"

# Output
print("Alphabet: \t\t\t" + "abcdefghijklmnopqrstuvwxyz")
print("Krypt. Alphabet: \t" + ciph_alph)
print("Klartext: \t\t\t" + input_text)
print("Cipher: \t\t\t" + monosub_enc(input_text, ciph_alph))
