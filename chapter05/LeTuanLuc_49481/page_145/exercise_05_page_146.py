"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: exercise_05_page_146.py
Problem:
    Assume that data refers to a list of numbers, and result refers to an empty list.
    Write a loop that adds the nonzero values in data to the result list, keeping them in their relative positions and excluding the zeros.
Solution:
    >>>
"""
data = [5, 0, 3, 7]
result = []
for element in data:
    if element !=0:
        result.append(element)
print(result)