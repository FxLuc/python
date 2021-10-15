"""
Author: Le Tuan Luc
Date: 2021/07/20
Program: exercise_04_page_85.py
Problem:
    Assume that the variables x and y refer to strings. Write a code segment that prints these strings in alphabetical order. You should assume that they are not equal.
Solution:
    >>>
"""
x = 'hello'
y = 'world'

def alphabetical_order(string):
    string_temp = []
    for character in string:
        string_temp.append(character)

    for i in range(0, len(string)):
        for j in range(0, len(string)):
            if string_temp[i] < string_temp[j]:
                temp_character = string_temp[i]
                string_temp[i] = string_temp[j]
                string_temp[j] = temp_character

    string_output = ""
    for character in string_temp:
        string_output += character

    return string_output

print(alphabetical_order(x+y))
    