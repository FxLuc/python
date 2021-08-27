"""
Author: Le Tuan Luc
Date: 2021/07/19
Program: exercise_04_page_70.py
Problem:
    Write a loop that prints the first 128 ASCII values followed by the corresponding characters (see the section on characters in Chapter 2).
    Be aware that most of the ASCII values in the range “0..31” belong to special control characters with no standard print representation, so you might see strange symbols in the output for these values.
Solution:
    >>>
"""
for count in range(0,128):
    print(f"{count}. {chr(count)}")