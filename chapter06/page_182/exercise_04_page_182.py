"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_04_page_182.py
Problem:
    Explain what happens when the following recursive function is called with the value 4 as an argument:
    def example(n):
        if n > 0:
            print(n)
            example(n - 1)
Solution:
    example(4)
        print(4)
        example(3)
            print(3)
            example(2)
                print(2)
                example(1)
                    print(1)
                    example(0)
                        False
"""