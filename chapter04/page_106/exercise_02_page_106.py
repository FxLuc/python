"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_02_page_106.py
Problem:
    Assume that the variable data refers to the string "myprogram.exe". Write the expressions that perform the following tasks:
        a. Extract the substring "gram" from data.
        b. Truncate the extension ".exe" from data.
        c. Extract the character at the middle position from data
Solution:
    a. data[data.find("gram"):data.find("gram")+4]
    b. data[:data.find(bad_character)]
    c. data[(len(data)-1)//2:(len(data)+2)//2]
"""
data = "myprogram.exe"

good_character = "gram"
print(data[data.find(good_character) : data.find(good_character) + len(good_character)])

bad_character = "exe"
print(data[:data.find(bad_character)])

print(data[(len(data)-1)//2:(len(data)+2)//2])