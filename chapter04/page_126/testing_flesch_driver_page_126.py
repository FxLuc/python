"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: casestudy_flesch_driver_page_126.py
Problem:
    Test driver for Flesch Index and Grade level.
Solution:
    >>>
"""
sentences = int(input("Sentences: "))
words = int(input("Words: "))
syllables = int(input("Syllables: "))

index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
print("Flesch Index:", index)

level = round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59)
print("Grade Level: ", level)