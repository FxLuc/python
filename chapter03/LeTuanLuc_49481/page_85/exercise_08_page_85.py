"""
Author: Le Tuan Luc
Date: 2021/07/20
Program: exercise_08_page_85.py
Problem:
    The variables x and y refer to numbers. Write a code segment that prompts the user for an arithmetic operator and prints the value obtained by applying that operator to x and y.
Solution:
    Input:
        X, Y (number)
        Arithmetic operator (string)
    If (Arithmetic operator == "+/-/*//")
    Result = X +/-/*// Y
    Output: print result
    >>>
"""
x = int(input('Enter any number: '))
y = int(input('Enter any number: '))
arithmetic_operator = input('Enter arithmetic operator: ')
if (arithmetic_operator == '+'):
    print(x+y)
if (arithmetic_operator == '-'):
    print(x-y)
if (arithmetic_operator == '*'):
    print(x*y)
if (arithmetic_operator == '/'):
    print(x/y)