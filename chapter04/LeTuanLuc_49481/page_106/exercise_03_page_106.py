"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_03_page_106.py
Problem:
    Assume that the variable myString refers to a string. Write a code segment that uses a loop to print the characters of the string in reverse order.
Solution:
    >>>
"""
my_string = input("Enter a string: ")

for index in range(len(my_string)-1, -1, -1):
    print(my_string[index], end="")

# print(my_string[::-1])