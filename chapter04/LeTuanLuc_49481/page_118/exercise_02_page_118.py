"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_02_page_118.py
Problem:
    Using the value of data from Exercise 1, write the values of the following expressions:
        a. data.endswith('i')
        b. " totally ".join(data.split())
Solution:
        a. False
        b. Python totally rules!
"""
data = "Python rules!"

print(data.endswith('i'))
print(" totally ".join(data.split()))