"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_03_page_62.py
Problem:
    Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums.
    The store rents new videos for $3.00 a night, and oldies for $2.00 a night.
    Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals.
    The program should prompt the user for the number of each type of video and output the total
cost.
Solution:
    1. Input the type.
    2. Compute the total charge using the formula
        total charge += costs of type videos rents.
    3. Print the total charge.
"""

# Initialize the constants
NEW_VIDEO_COSTS = 3.00
OLD_VIDEO_COSTS = 2.00

def total_charge(choise, total):
    if (choise == 1):
        total += OLD_VIDEO_COSTS
        print("-----------\nRents 1 oldies videos successfuly!\n-----------")
    elif (choise ==2):
        total += NEW_VIDEO_COSTS
        print("-----------\nRents 1 new videos successfuly!\n-----------")
    elif (choise == 3):
        # Display the total charge
        print(f"-----------\nTotal charge = {total}\n-----------")
    else:
        return
    menu(total)

# show menu and choise one
def menu(total):
    # Request the inputs
    choise = int(input("\n1. Rents oldies videos ($3.00)\n2. Rents new videos ($2.00)\n3. Show total charge\n4. Quit\nEnter your choise: "))
    total_charge(choise, total)

# total charge = 0
total = 0.0
menu(total)