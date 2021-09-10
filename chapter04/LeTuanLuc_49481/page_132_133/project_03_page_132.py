"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_03_page_132.py
Problem:
    Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.
Solution:
    >>>
"""
from os.path import exists


def decrypted_text(ord_value, distance):
    cipher_value = ord_value - distance
    return chr(cipher_value)


def encrypted_text(ord_value, distance):
    cipher_value = ord_value + distance
    return chr(cipher_value)


def crypt_text(plain_text, distance, is_encrypted):
    code = ""
    for character in plain_text:
        ord_value = ord(character)
        if ord_value == 32 or ord_value == 10:
            code += character
            continue
        if is_encrypted:
            code += encrypted_text(ord_value, distance)
        else:
            code += decrypted_text(ord_value, distance)
    return code


def open_text():
    file_name = input("Enter a file name: ")
    if not exists(file_name):
        print("Error: the file does not exist!")
        is_try_again = input("Try again? (y/n)")
        if is_try_again == "y" or is_try_again == "yes":
            open_text()
        else:
            return
    return open(file_name, 'r')


def main():
    f = open_text()
    distance = int(input("Enter the distance value: "))
    is_encrypted = input("Is encrypted file? (True/False)")
    print(crypt_text(f.read(), distance, is_encrypted))


if __name__ == "__main__":
    main()
