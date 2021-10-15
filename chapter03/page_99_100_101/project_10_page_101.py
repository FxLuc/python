"""
Author: Le Tuan Luc
Date: 2021/07/24
Program: project_10_page_101.py
Problem:
    The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%.
    Monthly payments are 5% of the listed purchase price, minus the down payment.
    Write a program that takes the purchase price as input.
    The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan.
    Each row of the table should contain the following items:
        - the month number (beginning with 1)
        - the current total balance owed
        - the interest owed for that month
        - the amount of principal owed for that month
        - the payment for that month
        - the balance remaining after payment
    The amount of interest for a month is equal to balance * rate / 12.
    The amount of principal for a month is equal to the monthly payment minus the interest owed.
Solution:
    >>>
"""
# Total price
price = float(input("Total computer cost: "))

# Price after down payment (10%)
remaining_price = (price * 0.9)

# Monthly payment (5%)
monthly_payment = remaining_price * 0.05

# Interest owed for this month (12% / 12 mount)
interest_owed = remaining_price * (.12/12.0)

# Principal for this month
principal = monthly_payment - interest_owed

# Month 
month = 0

# Print stuff
print("{:>10} {:>21} {:>21} {:>21} {:>21} {:>21}".format("Mouth", "Starting balance", "Interest to pay", "Principal to pay", "Payment", "Ending balance"))

while remaining_price > principal:
    month += 1
    interest_owed = remaining_price * (.12/12.0)
    principal = monthly_payment - interest_owed
    print("{:>10} {:>21.2f} {:>21.2f} {:>21.2f} {:>21.2f} {:>21.2f}".format(month, remaining_price, interest_owed, principal, monthly_payment, remaining_price - principal))
    remaining_price -= principal
