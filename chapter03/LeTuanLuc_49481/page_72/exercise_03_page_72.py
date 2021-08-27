"""
Author: Le Tuan Luc
Date: 2021/07/19
Program: exercise_03_page_72.py
Problem:
    Write a format operation that builds a string for the float variable amount that has exactly two digits of precision and a field width of zero.
Solution:
    field width = 0
    precision = 2
    >>>
"""
amount = 24.325
print ("%0.2f" % amount)