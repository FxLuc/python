"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_03_page_109.py
Problem:
    You are given a string that was encoded by a Caesar cipher with an unknown distance value.
    The text can contain any of the printable ASCII characters.
    Suggest an algorithm for cracking this code.
Solution:
    cipher_value = ord_value - distance
    if cipher_value < ord('a'):
        cipher_value = ord('z') - (ord('a') - cipher_value - 1)
"""
def encrypted_text(plain_text, distance):
    code = ""
    for character in plain_text:
        ord_value = ord(character)
        cipher_value = ord_value - distance
        if cipher_value < ord('a'):
            cipher_value = ord('z') - (ord('a') - cipher_value - 1)
        code = code + chr(cipher_value)
    return code

print(encrypted_text("sbwkrq", 3))
print(encrypted_text("kdfnhu", 3))
print(encrypted_text("abc", 3))