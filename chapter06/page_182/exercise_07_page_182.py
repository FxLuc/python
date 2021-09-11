"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_07_page_182.py
Problem:
    Explain what happens when the following recursive function is called with the values "hello" and 0 as arguments:
        def example(my_string, index):
            if index == len(my_string):
                return ""
            else:
                return my_string[index] + example(my_string, index + 1)
Solution:
    example("hello", 0)
            return "h" + example("hello", 1)
                return "e" + example("hello", 2)
                    return "l" + example("hello", 3)
                        return "l" + example("hello", 4)
                            return "o" + example("hello", 5)
                                return ""
"""