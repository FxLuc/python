"""
Author: Le Tuan Luc
Date: 2021/07/21
Program: project_04_page_99.py
Problem:
    Write a program that lets the user enter the initial height from which the ball is dropped and the number of times the ball is allowed to continue bouncing.
    Output should be the total distance traveled by the ball.
Solution:
    1. Input: height, times (int)
    2. BOUNCINESS = 0.6
    3. loop times:
        bounces = height * BOUNCINESS
        height += bounces
    4. Return height.
"""
def bouncing(height, times):
    BOUNCINESS = 0.6
    for i in range(times):
        bounces = height * BOUNCINESS
        height += bounces
    return height

height = int(input('Enter the initial height: '))
times = int(input('Enter the number of times: '))
print(bouncing(height, times))