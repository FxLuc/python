"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_05_page_114.py
Problem:
    Translate each of the following numbers to decimal numbers:
        a. 47
        b. 127
        c. AA
Solution:
        a. 71
        b. 295
        c. 170
"""
# using int()
def hex_to_dec(hex):
    return int(str(hex), 16)


# úing dictionary
def hex_to_dec(hex):
    HEX_TO_DEC_TABLE = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hex_string = str(hex).strip().upper()
    dec = 0
    length = len(hex_string) -1
    
    for digit in hex_string:
        dec += HEX_TO_DEC_TABLE[digit] * 16 ** length
        length -= 1
    
    return dec

print(hex_to_dec(47))
print(hex_to_dec(127))
print(hex_to_dec("AA"))