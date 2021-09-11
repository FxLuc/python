"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: exercise_02_page_145.py
Problem:
    Assume that the variable data refers to the list [5, 3, 7]. Write the expressions that perform the following tasks:
        a. Replace the value at position 0 in data with that value’s negation.
        b. Add the value 10 to the end of data.
        c. Insert the value 22 at position 2 in data.
        d. Remove the value at position 1 in data.
        e. Add the values in the list newData to the end of data.
        f. Locate the index of the value 7 in data, safely.
        g. Sort the values in data.
Solution:
    a. data[0] = -data[0]
    b. data.append(10)
    c. data.insert(2, 22)
    d. data.pop(1)
    e. data.extend(new_data)
    f. data.index(7)
    g. data.sort()
"""
