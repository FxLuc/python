"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_02_page_182.py
Problem:
    The factorial of a positive integer n, fact(n), is defined recursively as follows:
        fact( ) n 1 5 , when n 1 5
        fact( ) n n 5 2 * fact n( ) 1 , otherwise
        Define a recursive function fact that returns the factorial of a given positive integer.
Solution:
    Recursive design is a special case of top-down design, in which a complex problem is decomposed into smaller problems of the same form.
    Thus, the original problem is solved by a single recursive function.
"""


def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number-1)


def main():
    print(fact(5))


if __name__ == "__main__":
    main()
