"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_02_page_199.py
Problem:
    Write the code for a filtering that generates a list of the positive numbers in a list named numbers.
    You should use a lambda to create the auxiliary function.
Solution:
    >>>
"""


def main():
    numbers = [5, -6, 7, -8, -10]
    print(list(filter(lambda x: (x >= 0), numbers)))


if __name__ == "__main__":
    main()
