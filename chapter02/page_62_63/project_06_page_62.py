"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_06_page_62.py
Problem:
    The kinetic energy of a moving object is given by the formula KE = (1/2)mv^2 where m is the object’s mass and v is its velocity.
    Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum.
Solution:
    1. Input the mass (float).
    2. Input the velocity (float).
    3. Compute the kinetic energy of a moving object using the formula:
        kinetic energy = .5 * m * (v ** 2)
    4. Print the kinetic energy.
"""

def kinetic_energy(mass, velocity):
    ke = .5 * mass * (velocity ** 2)
    return ke

mass = float(input("Enter the mass (kilograms): "))
velocity = float(input("Enter the velocity (meters per second): "))
print(f"Kinetic energy= {kinetic_energy(mass, velocity)}")