def vigenere_dec(text, k):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    text = text.upper().replace(" ", "")
    k = k.upper().replace(" ", "")

    # Erweitert den Schlüssel so lange, bis er länger ist als der Klartext
    expanded_key = k
    while len(expanded_key) < len(text):
        # Hängt ein weiteres Mal den Schlüssel an
        expanded_key = expanded_key + k

    # Verschlüsselung anhand der Alphabetmatrix
    for i, char in enumerate(text):
        text_pos = alphabet.find(char)
        key_pos = alphabet.find(expanded_key[i])
        result += alphabet[(text_pos - key_pos) % 26]

    return result


# Text und Schlüssel hier ändern
cipher = "GEOUTKGIONQKLMOZBXGEUCBTMWJWUKLLFCG"
key = "Uebung"

# Output
Klartext = vigenere_dec(cipher, key)
print("Cipher: \t" + cipher)
print("Schlüssel: \t" + key)
print("Klartext: \t" + Klartext)
