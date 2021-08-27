"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: exercise_06_page_146.py
Problem:
    Write a loop that replaces each number in a list named data with its absolute value.
Solution:
    >>>
"""
data = [5, 0, -3, 7]
for element in data:
    if element < 0:
        data[data.index(element)] *= -1
print(data)