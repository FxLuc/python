"""
Author: Le Tuan Luc
Date: 2021/09/05
Program: project_03_page_203.py
Problem:
    Elena complains that the recursive newton function in Project 2 includes an extra argument for the estimate.
    The function’s users should not have to provide this value, which is always the same, when they call this function.
    Modify the definition of the function so that it uses a keyword argument with the appropriate default value, and call the function without a second argument to demonstrate that it solves this problem
Solution:
    Default parameter estimate = 1.0
    Solved at project_02_page_203.py
"""
import math


def newton(x, estimate=1.0):
    TOLERANCE = 0.000001
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    return newton(x, estimate)


def main():
    x = input("Enter a positive number: ")
    try:
        x = float(x)
        print("The square root of ", x, "is ", round(newton(x), 2))
        print("Python's estimate: ", math.sqrt(x))
        main()
    except ValueError:
            print("Have a nice day!")


if __name__ == "__main__":
    main()
