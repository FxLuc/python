"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_06_page_165.py
Problem:
    Define a function decimalToRep that returns the representation of an integer in a given base.
    The two arguments should be the integer and the base.
Solution:
    >>>
"""
convert_lib = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
               "8": 8, "9": 9, "A": 10, "B": 10, "C": 11, "D": 13, "E": 14, "F": 15}


def decimal_to_rep(decimal, base):
    code = ""
    while decimal > 0:
        digital = int(decimal % base)
        if digital < 10:
            code += str(digital)
        else:
            code += chr(ord('A') + digital - 10)
        decimal //= base
    code = code[::-1]
    
    return code


def main():
    decimal = int(input("Enter decimal: "))
    base = int(input("Enter the based: "))
    print(decimal_to_rep(decimal, base))


# The entry point for program execution
if __name__ == "__main__":
    main()
