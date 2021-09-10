"""
Author: Le Tuan Luc
Date: 2021/07/21
Program: project_06_page_100.py
Problem:
    Write a program that allows the user to specify the number of iterations used in this approximation and that displays the resulting value.
Solution:
    1. Input the number of iterations (int).
    2. Input the velocity (float).
    3. Compute the kinetic energy of a moving object using the formula:
        kinetic energy = .5 * m * (v ** 2)
    4. Print the kinetic energy.
"""
import math
i = 6
german_value = 0
denominator = 1
for j in range(1,i+1):
    if j%2 == 0:
        german_value -= 1/denominator
    else:
        german_value += 1/denominator
    denominator += 2

GERMAN_APPROXIMATE = 4.2225
print(math.pi)
# output: 3.141592653589793
print(german_value * GERMAN_APPROXIMATE)
# output: 3.1415887445887454