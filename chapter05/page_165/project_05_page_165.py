"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_05_page_165.py
Problem:
    Define a function named repToDecimal that expects two arguments, a string, and an integer.
    The second argument should be the base.
Solution:
    >>>
"""
convert_lib = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
               "8": 8, "9": 9, "A": 10, "B": 10, "C": 11, "D": 13, "E": 14, "F": 15}


def rep_to_decimal(code, base):
    code = code.upper()
    decimal = 0
    power = len(code) - 1
    for chr in code:
        decimal += convert_lib[chr] * (base ** power)
        power -= 1
    return decimal


def main():
    code = input("Enter code: ")
    base = int(input("Enter the based: "))
    print(rep_to_decimal(code, base))


# The entry point for program execution
if __name__ == "__main__":
    main()