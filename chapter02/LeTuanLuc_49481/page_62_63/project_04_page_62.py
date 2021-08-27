"""
Author: Le Tuan Luc
Date: 2021/07/13
Program: project_04_page_62.py
Problem:
    Write a program that takes the radius of a sphere (a floating-point number) as input
    and then outputs the sphere’s diameter, circumference, surface area, and volume.
Solution:
    1. Input the radius (float).
    2. Compute the sphere’s diameter using the formula:
        diameter = radius * 2
    3. Compute the circumference using the formula:
        circumference = diameter * PI
    4. Compute the surface area using the formula:
        surface area = (radius ** 2) * PI
    5. Compute the volume using the formula:
        volume = (radius ** 3) * .75 * PI
    6. Print the outputs.
"""
import math

def diameter(radius):
    radius *= 2
    return radius

def circumference(radius):
    circum =  diameter(radius) * math.pi
    return circum

def surface_area(radius):
    surface = (radius ** 2) * math.pi
    return surface

def volume(radius):
    vol = (radius ** 3) * 0.75 * math.pi
    return vol

radius = float(input("Enter the radius: "))
print(f"Diameter = {diameter(radius)}\nCircumference = {circumference(radius)}\nSurface area = {surface_area(radius)}\nVolume = {volume(radius)}")