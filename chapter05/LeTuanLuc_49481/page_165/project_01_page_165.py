"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_01_page_165.py
Problem:
    A group of statisticians at a local college has asked you to create a set of functions that compute the median and mode of a set of numbers, as defined in Section 5.4.
    Define these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers.
    Each function should expect a list of numbers as an argument and return a single number. Each function should return 0 if the list is empty.
    Include a main function that tests the three statistical functions with a given list.
Solution:
    >>>
"""


def mean(data):
    if len(data) == 0:
        return 0

    total = 0
    for number in data:
        total += number
    return total / len(data)


def mode(data):
    if len(data) == 0:
        return 0


def median(data):
    if len(data) == 0:
        return 0


def main():
    data = [1, 2, 3, 4, 5]
    print("list = ", data)
    print("Mean:", mean(data))


if __name__ == "__main__":
    main()
