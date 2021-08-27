"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_04_page_125.py
Problem:
    Write a code segment that prints the names of all of the items in the current working directory.
Solution:
    >>>
"""
import os

for name in os.listdir(os.getcwd()):
    print(name)