"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: exercise_04_page_149.py
Problem:
    Define a function named summation.
    This function expects two numbers, named low and high, as arguments.
    The function computes and returns the sum of the numbers between low and high, inclusive.
Solution:
    >>>
"""
def summation(low, high):
    result = 0
    for number in range(low, high+1):
        result += number
    return result

print(summation(2,5))