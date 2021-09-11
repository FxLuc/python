"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_04_page_106.py
Problem:
    Assume that the variable myString refers to a string, and the variable reversedString refers to an empty string.
    Write a loop that adds the characters from myString to reversedString in reverse order.
Solution:
    >>>
"""
my_string = input("Enter a string: ")

rev = ''
for character in my_string:
    rev = character + rev
print(rev)

# print(my_string[::-1])