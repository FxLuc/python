"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_05_page_182.py
Problem:
    Explain what happens when the following recursive function is called with the value 4 as an argument:
    def example(n):
        if n > 0:
            print(n)
            example(n)
        else:
            example(n - 1)
Solution:
    No way to break out of this function's recursion.
    example(4)
        print(4)
        example(4)
            print(4)
            example(4)
                print(4)
                example(4)
                    print(4)
                    example(4)
                        ...
                        Maximum recursion depth exceeded while calling a Python object
"""