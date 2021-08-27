"""
Author: Le Tuan Luc
Date: 2021/07/22
Program: project_07_page_100.py
Problem:
    Teachers in most school districts are paid on a schedule that provides a salary based on their number of years of teaching experience.
    For example, a beginning teacher in the Lexington School District might be paid $30,000 the first year.
    For each year of experience after this first year, up to 10 years, the teacher receives a 2% increase over the preceding value.
    Write a program that displays a salary schedule, in tabular format, for teachers in a school district.
    The inputs are the starting salary, the percentage increase, and the number of years in the schedule.
    Each row in the schedule should contain the year number and the salary for that year.
Solution:
    1. Input:
        the starting salary
        the percentage increase
        the number of years
    2. Using the formula:
        for i = 0 in range(number_of_years):
        each_year_salary = starting_salary * percentage_increase
        starting_salary += each_year_salary
    3. Return: i, each_year_salary, starting_salary
"""

starting_salary = int(input("Enter the starting salary: "))
percentage_increase = int(input("Enter the percentage increase: "))/100
number_of_years = int(input("Enter the number of years: "))

print("{:<5} {:<10} {:<15}".format("Year", "Increase", "Total"))
i = 0 
for i in range(number_of_years):
    each_year_salary = starting_salary * percentage_increase
    starting_salary += each_year_salary
    print("{:<5} {:<10} {:<15}".format(i + 1, round(each_year_salary,1), round(starting_salary,1)))