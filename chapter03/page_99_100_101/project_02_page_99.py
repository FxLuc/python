"""
Author: Le Tuan Luc
Date: 2021/07/21
Program: project_02_page_99.py
Problem:
    Write a program that accepts the lengths of three sides of a triangle as inputs.
    The program output should indicate whether or not the triangle is a right triangle.
    Recall from the Pythagorean theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides.
Solution:
    1. Input: a, b, c (number)
    2. Check right triagle: (a**2 == b**2 + c**2) or (c**2 == b**2 + a**2) or (b**2 == b**2 + a**2)
    3. Return boolean.
"""
def triangle_right(a,b,c):
    return (a**2 == b**2 + c**2) or (c**2 == b**2 + a**2) or (b**2 == b**2 + a**2)

a = int(input('Enter the length A: '))
b = int(input('Enter the length B: '))
c = int(input('Enter the length C: '))

print(triangle_right(a,b,c))