"""
Author: Le Tuan Luc
Date: 2021/07/21
Program: project_05_page_100.py
Problem:
    A local biologist needs a program to predict population growth.
    The inputs would be the initial number of organisms, the rate of growth (a real number greater than 0), the number of hours it takes to achieve this rate, and a number of hours during which the population grows. 
    Write a program that takes these inputs and displays a prediction of the total population.
Solution:
    1. Input:
        The initial number of organisms (int).
        The rate of growth (a real number greater than 0).
        The number of hours it takes to achieve this rate.
        A number of hours during which the population grows.
    2. Total population at growth_times 0 = organisms
    3. Compute the full-times using the formula:
        growth_times = hours_during // growth_period
    4. Compute population at each full-times using the formula:
        population *= growth_rate
    5. Compute the part-times using the formula:
        growth_times = hours_during % growth_period
    6. Compute population at part-times using the formula:
        population * (growth_times / growth_period)
    7. Output: total population = population full time + population part-time

"""
def prediction_population(organisms, growth_rate, growth_period, hours_during):
    growth_times = hours_during // growth_period
    population = organisms

    while growth_times > 0:
        population *= growth_rate
        growth_times -= 1

    growth_times = hours_during % growth_period
    population += population * (growth_times / growth_period)

    return population

organisms = int(input('Enter the initial number of organisms: '))
growth_rate = float(input('Enter a growth rate: '))
growth_period  = int(input('Enter the number of hours it takes to achieve that rate: '))
hours_during = int(input('Enter a number of hours during which the population grows: '))

print(prediction_population(organisms, growth_rate, growth_period, hours_during))