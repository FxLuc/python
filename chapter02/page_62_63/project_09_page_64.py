"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_09_page_63.py
Problem:
    Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles.
    Use the following approximations:
        A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
        There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
        A nautical mile is 1 minute of an arc.
Solution:
    1. Calc nautical miles using the formula:
        nautical miles = kilometers * degrees / minutes / 10000
    2. Print the nautical miles.
"""

def nautical_miles(kilometers):
    NAUTICAL_MILES = 90 * 60 / 10000.0
    return round(kilometers * NAUTICAL_MILES, 5)

kilometers = float(input("Enter the kilometers: "))
print(f"{kilometers} kilometers= {nautical_miles(kilometers)} nautical miles")