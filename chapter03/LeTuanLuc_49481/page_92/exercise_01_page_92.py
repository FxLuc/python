"""
Author: Le Tuan Luc
Date: 2021/07/20
Program: exercise_01_page_92.py
Problem:
    1. Translate the following for loops to equivalent while loops:
        a. for count in range(100):
        print(count)
        b. for count in range(1, 101):
        print(count)
        c. for count in range(100, 0, –1):
        print(count)
Solution:
    >>>
"""

# A
count = 0
while count < 100:
    print(count)
    count += 1

# B
count = 1
while count < 101:
    print(count)
    count += 1

# C
count = 100
while count > 0:
    print(count)
    count -= 1