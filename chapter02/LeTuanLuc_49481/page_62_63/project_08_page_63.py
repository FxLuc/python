"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_08_page_63.py
Problem:
    Light travels at 3*10^8 meters per second.
    A light-year is the distance a light beam travels in one year.
    Write a program that calculates and displays the value of a light-year.
Solution:
    1. Calc light-year using the formula:
        light-year = day in a year * hours in a day * minutes in a hours * second in a minutes * Light travels
    2. Print the light-year.
"""

def light_year():
    LIGHT_TRAVELS = 3 * (10 ** 8)
    return 365 * 24 * 60 * 60 * LIGHT_TRAVELS

print(f"The light-year= {light_year()} meters")