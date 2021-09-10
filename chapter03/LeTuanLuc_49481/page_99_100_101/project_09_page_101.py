"""
Author: Le Tuan Luc
Date: 2021/07/22
Program: project_09_page_101.py
Problem:
    Write a program that receives a series of numbers from the user and allows the user to press the enter key to indicate that he or she is finished providing inputs.
    After the user presses the enter key, the program should print the sum of the numbers and their average.
Solution:
    1.Input lenght of series of numbers
    2. While lenght of series of numbers > 0
        Input the number
        sum = sum + number input
        lenght of series of numbers - 1
    2. Calc average using the formula:
        sum of a series of numbers / lenght of series of numbers
    2. Print the average.
"""

lenght_of_series = int(input("Enter length of a series of numbers: "))
sum = 0
for i in range(lenght_of_series):
    sum += int(input(f"{i+1}.Enter the number: "))

print(sum/lenght_of_series)