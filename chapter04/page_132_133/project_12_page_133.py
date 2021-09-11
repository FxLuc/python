"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: project_12_page_133.py
Problem:
    The Payroll Department keeps a list of employee information for each pay period in a text file.
    The format of each line of the file is the following: <last name> <hourly wage> <hours worked>
    Write a program that inputs a filename from the user and prints to the terminal a report of the wages paid to the employees for the given period.
    The report should be in tabular format with the appropriate header.
    Each line should contain an employee’s name, the hours worked, and the wages paid for that period.
Solution:
    >>>
"""
from os.path import exists


def open_text(mode):
    file_name = input("Enter a file name: ")
    if not exists(file_name):
        print("Error: the file does not exist!")
        is_try_again = input("Try again? (y/n)")
        if is_try_again == "y" or is_try_again == "yes":
            open_text(mode)
        else:
            quit()
    return open(file_name, mode)


inputfile = open_text('r')
print('\n%-15s%-15s%-15s' % ('Last name', 'Hourly wage', 'Hours worked'))
for line in inputfile:
    dataList = line.split()
    name = str(dataList[0])
    hourly_wage = int(dataList[1])
    hours_worked = float(dataList[2])
    wages_paid = hourly_wage * hours_worked
    print('%-15s%-15d%-15.2f' % (name, hours_worked, wages_paid))
