import string
from caesar_cipher.util import check_english


# I read an article about enumerate in RealPython and now I'm in love
alphabet = {letter: i for i, letter in enumerate(string.ascii_lowercase)}
alphabet_numbers = {value: key for key, value in alphabet.items()}


def encrypt(plaintext, key):
    encrypted = ""
    for char in plaintext:
        if char.lower() in alphabet.keys():
            new_char = alphabet_numbers[(alphabet[char.lower()] + key) % 26]
            if char.isupper():
                new_char = new_char.upper()
            encrypted += new_char
        else:
            encrypted += char
    return encrypted


def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)


def crack(ciphertext):
    max_verified = [0, 0.0]
    for key in range(1, 26):
        curr_verified = check_english(decrypt(ciphertext, key))
        if curr_verified > max_verified[1]:
            max_verified[1] = curr_verified
            max_verified[0] = key
    if max_verified[1] < 0.4:
        return ""
    return decrypt(ciphertext, max_verified[0])
