"""
Author: Le Tuan Luc
Date: 2021/07/19
Program: exercise_03_page_85.py
Problem:
    Write a loop that counts the number of space characters in a string. Recall that the space character is represented as ' '.
Solution:
    >>>
"""

test_string = input("Enter the string value: ")
count = 0

for element in test_string:
  if element == " ":
       count+=1

print(count)