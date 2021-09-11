"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_04_page_114.py
Problem:
    Translate each of the following numbers to decimal numbers:
        a. 47
        b. 127
        c. 64
Solution:
        a. 39
        b. 87
        c. 52
"""
def oct_to_dec(octal):
    decimal_value, base = 0, 1
    while (octal): 
        last_digit = octal % 10
        octal = int(octal / 10)
        decimal_value += last_digit * base
        base = base * 8  
    return decimal_value

print(oct_to_dec(47))
print(oct_to_dec(127))
print(oct_to_dec(64))