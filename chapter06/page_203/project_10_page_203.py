"""
Author: Le Tuan Luc
Date: 2021/09/05
Program: project_10_page_203.py
Problem:
    Define and test a function myRange.
    This function should behave like Python’s standard range function, with the required and optional arguments, but it should return a list.
    Do not use the range function in your implementation!
Solution:
    >>>
"""
def my_range(start = None, stop = None, step = None):
    args = []
    for i in [start, stop, step]:
        if i is not None:
            args.append(i)

    step = 1
    if len(args) == 1:
        start = 0
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
        # default reverse step
        if start > stop: step = -1
    elif len(args) == 3:
        start, stop, step = args

    arr = []
    if step > 0:
        while start < stop:
            arr.append(start)
            start += step
    else:
        while start > stop:
            arr.append(start)
            start += step

    return arr


def main():
    print(" 2:", my_range(0, 10, 2))
    print(" 1:", my_range(0, 10))
    print(" 0:", my_range(10))
    print("-1:", my_range(10, 0))
    print("-2:", my_range(10, 0, -2))


if __name__ == "__main__":
    main()
