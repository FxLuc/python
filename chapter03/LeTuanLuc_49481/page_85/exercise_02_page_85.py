"""
Author: Le Tuan Luc
Date: 2021/07/19
Program: exercise_02_page_85.py
Problem:
    Assume that x refers to a number. Write a code segment that prints the number’s absolute value without using Python’s abs function.
Solution:
    Input: x (number)
    if x < 0:
        x *= (-1)
    Output: print x
    >>>
"""
x = -34.5645
def fake_abs(number):
    if 0 > number:
        return number * (-1)
    else:
        return number

print(fake_abs(x))