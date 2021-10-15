"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_02_page_62.py
Problem:
    Write a program that takes the length of an edge (an integer) as input and prints the cube’s surface area as output.
Solution:
    1. Input the length of an edge.
    2. Compute the cube’s surface area using the formula
        surface area = 6 * (length of an edge ** 2)
    3. Print the cube’s surface area.
"""

def surface_cubes(length_edge):
    # Compute the cube’s surface area
    surface_area = 6 * (length_edge ** 2)

    # Return value
    return surface_area

# Request the inputs
length_edge = int(input("Enter the length of an edge: "))

# Display the cube’s surface area
print("The cube’s surface area is: " + str(surface_cubes(length_edge)))