"""
Author: Le Tuan Luc
Date: 2021/07/20
Program: casestudy_incomtax_page_93.py
Problem:
    Compute the square root of a number.
Solution:
    1. The input is a number.
    2. The outputs are the program's estimate of the square root using Newton's method of successive approximations, and Python's own estimate using math.sqrt.
"""
import math

# Receive the input number from the user
x = float(input("Enter a positive number: "))

# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0

# Perform the successive approximations
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break

# Output the result
print("The program's estimate:", estimate)
print("Python's estimate: ", math.sqrt(x))
