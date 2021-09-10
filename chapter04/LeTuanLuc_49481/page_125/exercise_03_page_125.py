"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_03_page_125.py
Problem:
    Assume that a file contains integers separated by newlines. Write a code segment that opens the file and prints the average value of the integers.
Solution:
    >>>
"""
f = open("intFile.txt", 'r')
sum = count = 0
for value in f:
    sum += int(value)
    count += 1

print(sum/count)