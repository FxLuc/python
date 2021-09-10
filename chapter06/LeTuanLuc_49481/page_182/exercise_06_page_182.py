"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_06_page_182.py
Problem:
    Explain what happens when the following recursive function is called with the values "hello" and 0 as arguments:
    def example(my_string, index):
        if index < len(my_string):
            example(my_string, index + 1)
            print(my_string[index], end = "")
Solution:
    example("hello", 0)
        example("hello", 1)
            example("hello", 2)
                example("hello", 3)
                    example("hello", 4)
                        example("hello", 5)
                            False
                        print("o")
                    print("l")
                print("l")
            print("e")
        print("h")
"""