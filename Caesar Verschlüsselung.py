def caesar_enc(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Großbuchstaben verschlüsseln
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Kleinbuchstaben verschlüsseln
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


# Text und Verschiebung hier ändern
input_text = "Sicherheit"
shift = -4  # Alphabet der Verschlüsselung wird um shift nach links verschoben
# negatives Vorzeichen für Entschlüsselung bzw Verschiebung nach rechts

# Output
print("Klartext: \t\t" + input_text)
print("Shift pattern: " + str(shift))
print("Cipher: \t\t" + caesar_enc(input_text, shift))
