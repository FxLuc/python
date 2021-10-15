"""
Author: Le Tuan Luc
Date: 2021/10/08
Program: IT19A2B_LeTuanLuc_49481_cau01.py
Problem: Write program to find all roots of a quadratic equation.
Input: a, b, c
Calc:
    determinant = b2-4ac
    root1 = (-b + √(determinant))/(2a)
    root2 = (-b - √(determinant))/(2a)
Output:
    if determinant > 0, roots are real and distinct
    if determinant == 0, roots are real and same
    if determinant < 0, roots are complex number and distinct
"""
from math import sqrt

def solve_quadratic_equations(a, b, c):
    if (a == 0):
        if (b == 0):
            return f"The roots are not real."
        return f"The root is real: \nx = {(-c / b): .2f}"
 
    determinant = b * b - 4 * a * c
    if (determinant > 0):
        x1 = (float)((-b + sqrt(determinant)) / (2 * a))
        x2 = (float)((-b - sqrt(determinant)) / (2 * a))
        return f"The roots are real and distinct: \nx1 = {x1: .2f}\nx2 = {x2: .2f}"

    elif (determinant == 0):
        x1 = (-b / (2 * a))
        return f"The roots are real and same: \nx1 = x2 = {x1: .2f}"

    else:
        real = (float)(-b / (2 * a))
        imaginary = (float)(sqrt(-determinant) / (2 * a))
        return f"The roots are complex number and distinct: \nx1 = {real: .2f} +{imaginary: .2f}i \nx2 = {real: .2f} -{imaginary: .2f}i"


def main():
    print("\nax^2 + bx + c")
    try:
        a = float(input("Enter a number (a):"))
        b = float(input("Enter a number (b):"))
        c = float(input("Enter a number (c):"))
        print(solve_quadratic_equations(a, b, c))
    except ValueError:
        print("a,b,c requires input must be a number!")
        main()


if __name__ == "__main__":
    main()