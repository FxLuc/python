"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_01_page_125.py
Problem:
    Write a code segment that opens a file named myfile.txt for input and prints the number of lines in the file.
Solution:
    >>>
"""

f = open("myFile.txt", 'r')
count = 0
for line in f:
    print(line)
    count += 1

print("Number of lines in the file:", count)