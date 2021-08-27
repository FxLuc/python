"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: exercise_08_page_146.py
Problem:
    Explain the difference between structural equivalence and object identity
Solution:
    For example, you might want to determine whether one variable is an alias for another.
    The == operator returns True if the variables are aliases for the same object.
    Unfortunately, == also returns True if the contents of two different objects are the same.
    The first relation is called object identity, whereas the second relation is called structural equivalence.
    The == operator has no way of distinguishing between these two types of relations.
    Python’s is operator can be used to test for object identity.
    It returns True if the two operands refer to the exact same object, and it returns False if the operands refer to distinct objects (even if they are structurally equivalent
"""