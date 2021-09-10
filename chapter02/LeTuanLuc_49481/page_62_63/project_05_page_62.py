"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_05_page_62.py
Problem:
    An object’s momentum is its mass multiplied by its velocity.
    Write a program that accepts an object’s mass (in kilograms) and velocity (in meters per second) as inputs and then outputs its momentum.
Solution:
    1. Input the mass (float).
    2. Input the velocity (float).
    3. Compute the momentum using the formula:
        momentum = mass * velocity
    4. Print the momentum.
"""

def diameter(mass, velocity):
    momentum = mass * velocity
    return momentum

mass = float(input("Enter the mass (kilograms): "))
velocity = float(input("Enter the velocity (meters per second): "))
print(f"Momentum= {diameter(mass, velocity)}")