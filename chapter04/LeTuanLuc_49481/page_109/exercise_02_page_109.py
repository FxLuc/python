"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_02_page_109.py
Problem:
    Consult the Table of ASCII values in Chapter 2 and suggest how you would modify the encryption and decryption scripts in this section to work with strings containing all of the printable characters.
Solution:
    if cipher_value > ord('z'):
        cipher_value = ord('a') + distance - (ord('z') - ord_value + 1)
"""
def encrypted_text(plain_text, distance):
    code = ""
    for character in plain_text:
        ord_value = ord(character)
        cipher_value = ord_value + distance
        if cipher_value > ord('z'):
            cipher_value = ord('a') + distance - (ord('z') - ord_value + 1)
        code = code + chr(cipher_value)
    return code

print(encrypted_text("python", 3))
print(encrypted_text("hacker", 3))
print(encrypted_text("wow", 3))

plainText = input("Enter text to encrypt: ")
distance = int(input("Enter the distance value: "))
print(encrypted_text(plainText, distance))