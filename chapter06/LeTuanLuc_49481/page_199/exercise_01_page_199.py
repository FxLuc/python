"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_01_page_199.py
Problem:
    Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers.
Solution:
    >>>
"""


def main():
    numbers = [5, -6, 7, -8, -10]
    print(list(map(abs, numbers)))


if __name__ == "__main__":
    main()
