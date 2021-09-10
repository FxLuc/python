"""
Author: Le Tuan Luc
Date: 2021/07/19
Program: exercise_02_page_72.py
Problem:
    Write a code segment that displays the values of the integers x, y, and z on a single line, such that each value is right-justified with a field width of 6.
Solution:
    print("%6s" % <variable>)
    >>>
"""
x = 123
y = 43
z = 56789
print("|%6s" % x, "|%6s" % y, "|%6s" % z)