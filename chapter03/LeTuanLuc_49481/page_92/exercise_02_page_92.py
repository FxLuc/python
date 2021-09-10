"""
Author: Le Tuan Luc
Date: 2021/07/20
Program: exercise_02_page_92.py
Problem:
    The factorial of an integer N is the product of the integers between 1 and N, inclusive. Write a while loop that computes the factorial of a given integer N.
Solution:
    >>>
"""
def factorial(number):
    if 0 > number:
        return 'wrong number'
    else:
        i = 0
        factorial_number = 1
        while i < number:
            i += 1
            factorial_number *= i
        return factorial_number

print(factorial(7))