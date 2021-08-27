"""
Author: Le Tuan Luc
Date: 2021/07/12
Program: casestudy_incomtax_page_38.py
Problem:
    The customer requests a program that computes a person’s income tax.
    Input the gross income and number of dependents
    Compute the taxable income using the formula
    Taxable income = gross income - 10000 - (3000 * number of dependents)
    Compute the income tax using the formula
    Tax = taxable income * 0.20
    Print the tax
Solution:
    1. Significant constants
        tax rate
        standard deduction
        deduction per dependent
    2. The inputs are
        gross income
        number of dependents
    3. Computations:
        taxable income = gross income - the standard deduction - a deduction for each dependent
        income tax = is a fixed percentage of the taxable income
    4. The outputs are
        the income tax
"""

def incomtax(gross_income, num_dependents):
    # Initialize the constants
    TAX_RATE = 0.20
    STANDARD_DEDUCTION = 10000.0
    DEPENDENT_DEDUCTION = 3000.0

    # Compute the income tax
    taxable_income = gross_income - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * num_dependents
    income_tax = taxable_income * TAX_RATE

    # Return the income tax
    return income_tax

# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Display the income tax
print("The income tax is $" + str(incomtax(grossIncome, numDependents)))