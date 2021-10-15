"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_01_page_114.py
Problem:
    Translate each of the following numbers to decimal numbers:
        a. 11001
        b. 100000
        c. 11111
Solution:
    a. 25
    b. 32
    c. 31
"""
def bin_to_dec(binary):
    decimal = 0
    binary = str(binary)
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

print(bin_to_dec(11001))
print(bin_to_dec(100000))
print(bin_to_dec(11111))