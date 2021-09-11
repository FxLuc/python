"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_10_page_63.py
Problem:
    An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay.
    Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.
    Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay.
Solution:
    1. Calc total weekly pay using the formula:
        total weekly pay = (total overtime hours * 1.5 + total regular hours) * hourly wage
    2. Print total weekly pay.
"""

def weekly_pay(hourly_wage, total_regular_hours, total_overtime_hours):
    OVERTIME_PAY = 1.5
    return (total_overtime_hours * OVERTIME_PAY + total_regular_hours) * hourly_wage

hourly_wage = float(input("Enter the hourly wage: $"))
total_regular_hours = float(input("Enter the total regular hours: "))
total_overtime_hours = float(input("Enter the total overtime hours: "))
print(f"An employee’s total weekly pay= ${weekly_pay(hourly_wage, total_regular_hours, total_overtime_hours)}")