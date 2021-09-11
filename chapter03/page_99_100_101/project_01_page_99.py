"""
Author: Le Tuan Luc
Date: 2021/07/21
Program: project_01_page_99.py
Problem:
    Write a program that accepts the lengths of three sides of a triangle as inputs.
    The program output should indicate whether or not the triangle is an equilateral triangle.
Solution:
    1. Input: a, b, c (number)
    2. Check equilateral triagle: a == b == c
    3. Return boolean.
"""
def triangle_equilateral(a,b,c):
    return a == b == c

a = int(input('Enter the length A: '))
b = int(input('Enter the length B: '))
c = int(input('Enter the length C: '))

print(triangle_equilateral(a,b,c))