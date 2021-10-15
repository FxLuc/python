"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_04_page_199.py
Problem:
    Modify the summation function presented in Section 6.2 so that it includes default arguments for a step value and a function.
    The step value is used to move to the next value in the range.
    The function is applied to each number visited, and thefunction’s returned value is added to the running total.
    The default step value is 1, and the default function is lambda that returns its argument (essentially an identity function).
    An example call of this function is summation (l, 100, 2, math.sqrt), which returns the sum of the square roots of every other number between 1 and 100.
    The function can also be called as usual, with just the bounds of the range.
Solution:
    >>>
"""
from functools import reduce
import math


def summation(lower, upper, step=1, calculation=int):
    if lower > upper:
        return 0
    else:
        return reduce(lambda x, y: calculation(x) + calculation(y), range(lower, upper, step))


def main():
    print(summation(0, 10, 1, math.sqrt))


if __name__ == "__main__":
    main()
