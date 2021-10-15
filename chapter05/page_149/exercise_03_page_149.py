"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: exercise_03_page_149.py
Problem:
    Use the function even to simplify the definition of the function odd presented in this section.
Solution:
    >>>
"""
def even(number):
    if (number % 2 == 0):
        return True
    return False

def odd(number):
    if even(number):
        return False
    return True