"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_02_page_132.py
Problem:
    Write a script that inputs a line of encrypted text and a distance value and outputs plaintext using a Caesar cipher.
    The script should work for any printable characters.
Solution:
    >>>
"""


def decrypted_text(plain_text, distance):
    code = ""
    for character in plain_text:
        if character == " ":
            code += character
            continue
        ord_value = ord(character)
        cipher_value = ord_value - distance
        if cipher_value < ord('a') and cipher_value > ord('Z') or cipher_value < ord('A'):
            cipher_value = ord('z') - (ord('a') - cipher_value - 1)
        code += chr(cipher_value)
    return code


def main():
    plain_text = input("Enter text to decrypt: ")
    distance = int(input("Enter the distance value: "))
    print(decrypted_text(plain_text, distance))


if __name__ == "__main__":
    main()
