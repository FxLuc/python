"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_02_page_125.py
Problem:
    Write a code segment that opens a file for input and prints the number of four-letter words in the file.
Solution:
    >>>
"""

f = open("myFile.txt", 'a')
f.write("\nabcd")

f = open("myFile.txt", 'r')
print(f.read())