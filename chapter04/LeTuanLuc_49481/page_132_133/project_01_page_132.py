"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_01_page_132.py
Problem:
    Write a script that inputs a line of plaintext and a distance value and outputs an encrypted text using a Caesar cipher.
    The script should work for any printable characters.
Solution:
    >>>
"""


def encrypted_text(plain_text, distance):
    code = ""
    for character in plain_text:
        if character == " ":
            code += character
            continue
        ord_value = ord(character)
        cipher_value = ord_value + distance
        if cipher_value > ord('Z') and cipher_value < ord('a') or cipher_value > ord('z'):
            cipher_value = ord('a') + distance - (ord('z') - ord_value + 1)
        code += chr(cipher_value)
    return code


def main():
    plain_text = input("Enter text to encrypt: ")
    distance = int(input("Enter the distance value: "))
    print(encrypted_text(plain_text, distance))


if __name__ == "__main__":
    main()
