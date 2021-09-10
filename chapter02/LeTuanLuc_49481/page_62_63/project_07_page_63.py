"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_07_page_63.py
Problem:
    Write a program that calculates and prints the number of minutes in a year.
Solution:
    1. Input the year (int).
    2. Check leap year using the formula:
        return true if: ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
    2. Compute the number of minutes in a year using the formula:
        minutes = day in a year * 24 * 60
    3. Print the number of minutes in a year.
"""

def check_leap_year(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

def minutes_in_year(year):
    if (check_leap_year(year)):
        minutes = 366 * 24 * 60
    else:
        minutes = 365 * 24 * 60
    return minutes

year = int(input("Enter the year: "))
print(f"The number of minutes in a year= {minutes_in_year(year)}")