"""
Author: Le Tuan Luc
Date: 2021/07/20
Program: exercise_03_page_92.py
Problem:
    The log 2 of a given number N is given by M in the equation N = 2^M.
    Using integer arithmetic, the value of M is approximately equal to the number of times N can be evenly divided by 2 until it becomes 0.
    Write a loop that computes this approximation of the log 2 of a given number N.
Solution:
    >>>
"""
import math
def log_fake(number):
    STEP = 1/100000
    m = 0
    while (2 ** m) < number:
        m += STEP
    return round(m,5)

print(log_fake(934893458))
# output: 29.80023

print(math.log(934893458,2))
#  output: 29.8002267215611