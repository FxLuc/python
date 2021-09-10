"""
Author: Le Tuan Luc
Date: 2021/09/05
Program: project_05_page_203.py
Problem:
    A list is sorted in ascending order if it is empty or each item except the last one is less than or equal to its successor.
    Define a predicate isSorted that expects a list as an argument and returns True if the list is sorted, or returns False otherwise.
Solution:
    >>>
"""


def is_sorted(arr, is_ascending=True):
    if len(arr) < 2:
        return True
    if is_ascending:
        return is_sorted_ascending(arr)
    return is_sorted_descending(arr)


def is_sorted_ascending(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True


def is_sorted_descending(arr):
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            return False
    return True


def main():
    data = [1, 2, 3, 4, 5, ]
    print(is_sorted(data))
    data = [5, 4, 3, 2, 1, ]
    print(is_sorted(data, False))


if __name__ == "__main__":
    main()
