"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: exercise_01_page_145.py
Problem:
    Assume that the variable data refers to the list [5, 3, 7]. Write the values of the following expressions:
        a. data[2]
        b. data[-1]
        c. len(data)
        d. data[0:2]
        e. 0 in data
        f. data + [2, 10, 5]
        g. tuple(data)
Solution:
    a. 7
    b. 7
    c. 3
    d. [5, 3]
    e. False
    f. [5, 3, 7, 2, 10, 5]
    g. (5, 3, 7)
"""
data = [5, 3, 7]
print(data[2])
print(data[-1])
print(len(data))
print(data[0:2])
print(0 in data)
print(data + [2, 10, 5])
print(tuple(data))