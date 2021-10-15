"""
Author: Le Tuan Luc
Date: 2021/07/19
Program: exercise_02_page_70.py
Problem:
    Write a loop that prints your name 100 times. Each output should begin on a new line.
Solution:
    Input: YOUR_NAME (string)
    FOR loop 0->100:
        print YOUR_NAME
    Output: prints your name 100 times.
"""
YOUR_NAME = input("Enter your name: ")
for count in range(0, 100):
    print(YOUR_NAME)