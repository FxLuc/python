"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_01_page_62.py
Problem:
    The tax calculator program of the case study outputs a floating-point number that might show more than two digits of precision
    Use the round function to modify the program to display at most two digits of precision in the output number.
Solution:
    Add the round function at incom tax return value.
"""

def incomtax(gross_income, num_dependents):
    # Initialize the constants
    TAX_RATE = 0.20
    STANDARD_DEDUCTION = 10000.0
    DEPENDENT_DEDUCTION = 3000.0

    # Compute the income tax
    taxable_income = gross_income - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * num_dependents
    income_tax = taxable_income * TAX_RATE

    # Return the income tax using the round function
    return round(income_tax, 2)

# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Display the income tax
print("The income tax is $" + str(incomtax(grossIncome, numDependents)))