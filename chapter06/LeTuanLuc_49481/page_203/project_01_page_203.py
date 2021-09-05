"""
Author: Le Tuan Luc
Date: 2021/09/05
Program: project_01_page_203.py
Problem:
    Package Newton’s method for approximating square roots (Case Study 3.6) in a function named newton.
    This function expects the input number as an argument and returns the estimate of its square root.
    The script should also include a main function that allows the user to compute square roots of inputs until she presses the enter/return key.
Solution:
    >>>
"""
import math


def newton(x):
    TOLERANCE = 0.000001
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= TOLERANCE:
            break
    return estimate


def main():
    while True:
        x = input("Enter a positive number: ")
        try:
            x = float(x)
            print("The square root of ", x, "is ", round(newton(x), 2))
            print("Python's estimate: ", math.sqrt(x))
        except ValueError:
            break


if __name__ == "__main__":
    main()
