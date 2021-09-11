"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_01_page_118.py
Problem:
    Assume that the variable data refers to the string "Python rules!". Use a string method from Table 4-2 to perform the following tasks:
        a. Obtain a list of the words in the string.
        b. Convert the string to uppercase.
        c. Locate the position of the string "rules".
        d. Replace the exclamation point with a question mark.
Solution:
    a. split()
    b. upper()
    c. find("rules")
    d. replace(old, new [, count])
"""
data = "Python rules!"

print(data.split())
print(data.upper())
print(data.find("rules"))
print(data.replace("!", "?"))