"""
Author: Le Tuan Luc
Date: 2021/07/20
Program: exercise_06_page_85.py
Problem:
    Construct truth tables for the following Boolean expressions:
        a. not (A or B)
        b. not A and not B
Solution:
    >>>
"""
from tabulate import tabulate


table = []
table.append(['A', 'B', 'not (A or B)', 'not A and not B'])
A = False
B = False
table.append([A, B, not (A or B), not A and not B])
A = True
B = False
table.append([A, B, not (A or B), not A and not B])
A = False
B = True
table.append([A, B, not (A or B), not A and not B])
A = True
B = True
table.append([A, B, not (A or B), not A and not B])
print(tabulate(table, headers='firstrow', tablefmt='grid'))