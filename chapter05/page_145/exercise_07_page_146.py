"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: exercise_07_page_146.py
Problem:
    Describe the costs and benefits of aliasing, and explain how it can be avoided.
Solution:
    Assignment of one variable to another variable causes both variables to refer to the same data object.
    When two or more variables refer to the same data object, they are aliases.
    When that data value is a mutable object such as a list, side effects can occur.
    A side effect is an unexpected change to the contents of a data object.
    To prevent side effects, avoid aliasing by assigning a copy of the original data object to the new variable.
"""