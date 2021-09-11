"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_03_page_194.py
Problem:
    What is the lifetime of a variable? Give an example
Solution:
    The lifetime of a variable is the duration of program execution during which it uses memory storage.
    Module variables exist for the lifetime of the program that uses them.
    Parameters and temporary variables exist for the lifetime of a particular function call.
    Example:
        get_value():
            a = 5
            a += 15
            return a
        In the above function the integer a is created as soon ad the function is called and destroyed after the last statement is executed.
        That is why if you return the address of a from this function and try to use it, you would see undefined behaviour as the memory used by a is already marked for deletion.
"""