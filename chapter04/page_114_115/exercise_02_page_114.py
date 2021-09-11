"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_02_page_114.py
Problem:
    Translate each of the following numbers to binary numbers:
        a. 47
        b. 127
        c. 64
Solution:
    a. 101111
    b. 1111111
    c. 1000000
"""
def dec_to_bin(decimal):
    if decimal > 1:
        dec_to_bin(decimal // 2)
    print(decimal % 2, end="")

dec_to_bin(64)