"""
Author: Le Tuan Luc
Date: 2021/07/03
Program: page_033_projects_08.py
Problem:
    Enter an input statement using the input function at the shell prompt.
    When the prompt asks you for input, enter a number.
    Then, attempt to add 1 to that number, observe the results, and explain what happened.
Solution:
    TypeError: can only concatenate str (not "int") to str
    -> Whatever we enter as input, input function convert it into a string.
    -> Can only sum numberic data type (integers, floats,...) or concatenate string data type to string data type.
    
    >>> num = float(input('Enter any number: '))
    or
    >>> print(float(num) + 1)
"""
num = input('Enter any number: ')
print(num + 1)