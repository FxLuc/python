"""
Author: Le Tuan Luc
Date: 2021/09/05
Program: project_04_page_203.py
Problem:
    Restructure Newton’s method (Case Study 3.6) by decomposing it into three cooperating functions.
    The newton function can use either the recursive strategy of Project 1 or the iterative strategy of Case Study 3.6.
    The task of testing for the limit is assigned to a function named limitReached,
    whereas the task of computing a new approximation is assigned to a function named improveEstimate.
    Each function expects the relevant arguments and returns an appropriate value.
Solution:
    >>>
"""
import math


def limit_reached(x, estimate):
    TOLERANCE = 0.000001
    return abs(x - improve_estimate(x, estimate) ** 2) <= TOLERANCE


def improve_estimate(x, estimate):
    return (estimate + x / estimate) / 2


def newton(x, estimate=1.0):
    if limit_reached(x, estimate):
        return improve_estimate(x, estimate)
    return newton(x, improve_estimate(x, estimate))


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
