"""
Author: Le Tuan Luc
Date: 2021/09/05
Program: project_02_page_203.py
Problem:
    Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton. 
Solution:
    >>>
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
