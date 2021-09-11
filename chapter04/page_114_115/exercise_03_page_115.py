"""
Author: Le Tuan Luc
Date: 2021/08/02
Program: exercise_03_page_115.py
Problem:
    Translate each of the following numbers to binary numbers:
        a. 47
        b. 127
        c. 64
Solution:
        a. 100111
        b. 001010111
        c. 110100
"""
def oct_to_bin_equivalent(octal):
    binary = ""
    while octal!=0:
        rem = octal % 10
        if rem==0:
            binary += "000"
        elif rem==1:
            binary += "001"
        elif rem==2:
            binary += "010"
        elif rem==3:
            binary += "011"
        elif rem==4:
            binary += "100"
        elif rem==5:
            binary += "101"
        elif rem==6:
            binary += "110"
        elif rem==7:
            binary += "111"
        octal = int(octal/10)
    return binary

def oct_to_bin(octal):
    rev = chk = 0
    while octal!=0:
        rem = octal % 10
        if rem > 7:
            chk = 1
            break
        rev = rem + (rev * 10)
        octal = int(octal / 10)
    if chk == 0:
        octal = rev
        return oct_to_bin_equivalent(octal)
    else:
        return "Invalid Input!"

print(oct_to_bin(64))