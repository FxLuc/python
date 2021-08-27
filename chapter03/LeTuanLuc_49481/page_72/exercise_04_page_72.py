"""
Author: Le Tuan Luc
Date: 2021/07/19
Program: exercise_04_page_72.py
Problem:
    Write a loop that outputs the numbers in a list named salaries. The outputs should be formatted in a column that is right-justified, with a field width of 12 and a precision of 2.
Solution:
    >>>
"""
salaries = (1.445, 4.8764, 5.2445, 5.6789, 6.324663, 6.887986, 8.3535)
for element in salaries:
    print("%12.2f" % element)