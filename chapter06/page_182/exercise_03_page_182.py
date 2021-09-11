"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_03_page_182.py
Problem:
    Describe the costs and benefits of defining and using a recursive function.
Solution:
    The run-time system on a real computer, such as the PVM, must devote some overhead to recursive function calls.
    At program startup, the PVM reserves an area of memory named a call stack.
    For each call of a function, recursive or otherwise, the PVM must allocate on the call stack a small chunk of memory called a stack frame.
    In this type of storage, the system places the values of the arguments and the return address for each function call.
    Space for the function call’s return value is also reserved in its stack frame.
    When a call returns or completes its execution, the return address is used to locate the next instruction in the caller’s code, and the memory for the stack frame is deallocated.
    When a function invokes hundreds or even thousands of recursive calls, the amount of extra resources required, both in processing time and in memory usage, can add up to a significant performance hit.
    When, because of a design error, the recursion is infinite, the stack frames are added until the PVM runs out of memory, which halts the program with an error message.
"""