def otp_enc(text, k):
    result = ""
    for i in range(len(text)):
        c = bool(int(text[i])) ^ bool(int(k[i]))
        result += str(int(c))
    return result


# Text und Schlüssel hier ändern
Klartext = "01000111010011110100010101"
key = "01010011010010010100001101"

# Output
print("Klartext: \t" + Klartext)
print("Schlüssel: \t" + str(key))
print("Cipher: \t" + otp_enc(Klartext, key))
