"""
Author: Le Tuan Luc
Date: 2021/07/19
Program: exercise_05_page_70.py
Problem:
    Assume that the variable teststring refers to a string.
    Write a loop that prints each character in this string, followed by its ASCII value.
Solution:
    >>>
"""
test_string = 'string'
for character in test_string:
    print(f"{character} - {ord(character)}")