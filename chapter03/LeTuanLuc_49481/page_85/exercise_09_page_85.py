"""
Author: Le Tuan Luc
Date: 2021/07/20
Program: exercise_08_page_85.py
Problem:
    Does the Boolean expression count > 0 and total // count > 0 contain a potential error? If not, why not?
Solution:
    Assuming that all the necessary declarations are made and given statements are only an extract, we can conclude that the given piece of code contains error.
    'count > 0': This statement is right if we match this with the syntax of regular comparison operation. Here count is an operand, “0” is the constant operand and these two operands are operated by the operator “>”.
    When we take 'total // count > 0': Here 'count > 0' returns Boolean and 'total' is assumed to be an integer, and an integer cannot be divided by a Boolean value.
    So it can be rectified as '(total / count) > 0'. 
"""
