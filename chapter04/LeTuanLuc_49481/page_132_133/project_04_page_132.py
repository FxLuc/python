"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_04_page_132.py
Problem:
    Write the scripts octalToDecimal.py and decimalToOctal.py, which convert numbers between the octal and decimal representations of integers.
Solution:
    >>>
"""


def octal_to_decimal(octal):
    decimal_value, base = 0, 1
    while (octal):
        last_digit = octal % 10
        octal = int(octal / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value


def decimal_to_octal(decimal):
    octal_value = 0
    i = 1
    while (decimal != 0):
        octal_value += (decimal % 8) * i
        decimal = int(decimal / 8)
        i *= 10
    return octal_value


def main():
    print(octal_to_decimal(47))
    print(decimal_to_octal(39))


if __name__ == "__main__":
    main()
