"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_06_page_133.py
Problem:
    Use the strategy of the decimal to binary conversion and the bit shift left operation defined in Project 5 to code a new encryption algorithm.
    The algorithm should add 1 to each character’s numeric ASCII value, convert it to a bit string, and shift the bits of this string one place to the left.
    A single-space character in the encrypted string separates the resulting bit strings.
Solution:
    >>>
"""
import binascii

def encrypted_string(bit_string):
    code = ""
    for character in bit_string:
        code += f"{ord(chr(ord(character) + 1)):08b}"
    return code[1:] + code[0]


def main():
    bit_string = input("Enter a bit string: ")
    print(encrypted_string(bit_string))


if __name__ == "__main__":
    main()
