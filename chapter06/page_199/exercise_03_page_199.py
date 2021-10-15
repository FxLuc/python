"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_03_page_199.py
Problem:
    Write the code for a reducing that creates a single string from a list of strings named words.
Solution:
    >>>
"""
from functools import reduce


def main():
    words = ['h', 'a', 's', 'a', 'g', 'i']
    print(reduce(lambda x, y: x + y, words))


if __name__ == "__main__":
    main()
