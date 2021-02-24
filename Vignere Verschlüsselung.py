import re
import math

from pip._vendor.msgpack.fallback import xrange


def vigenere_enc(text, k):
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
        result += alphabet[(text_pos + key_pos) % 26]

    return result


# Text und Schlüssel hier ändern
Klartext = "Management der Informationssicherheit"
key = "Uebung"

# Output
cipher = vigenere_enc(Klartext, key)
print("Klartext: \t" + Klartext)
print("Schlüssel: \t" + key)
print("Cipher: \t" + cipher)


print("\n-----Kasiski Angriff zur Ermittelung der maximalen Schlüssellänge-----")


def search(array, bigram):
    indices = []
    for i in range(len(array)):
        if array[i] == bigram:
            indices.append(i)
    return indices


def vignere_keylen_max(text):
    repeated_sequences = dict()
    bigrams = re.findall(r'(?=([a-zA-Z]{2}))', text)
    for bigram in bigrams:
        idx = search(bigrams, bigram)
        if len(idx) > 1:
            repeated_sequences[bigram] = int(idx[1]) - int(idx[0])
    return repeated_sequences


def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


# Output
print(vignere_keylen_max(cipher))
print("Mögliche Schlüssellängen:", list(divisorGenerator(18)))
