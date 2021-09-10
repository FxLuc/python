"""
Author: Le Tuan Luc
Date: 2021/07/22
Program: project_08_page_100.py
Problem:
    The greatest common divisor of two positive integers.
Solution:
    1. Input:
        number A
        number B
    2. Compute the remainder of dividing the larger number by the smaller number.
    3. Replace the larger number with the smaller number and the smaller number with the remainder.
    4. Repeat this process until the smaller number is zero.
"""

x = int(input("Enter number A:"))
y = int(input("Enter number B:"))

def gcd(x, y):
    if (y == 0):
        return x
    else:
        return gcd(y, (x % y))

print(gcd(x, y))