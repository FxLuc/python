"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: exercise_02_page_194.py
Problem:
    What is the scope of a variable? Give an example.
Solution:
    The scope of a variable is the area of program text within which it has a given value.
    The scope of a module variable is the text of the module below the variable’s introduction and the bodies of any function definitions.
    The scope of a parameter is the body of its function definition. The scope of a temporary variable is the text of the function body below its introduction.
    Example: 
        The scope of the module variables replacements and change_person includes the entire module below the point where the variables are introduced.
        This includes the code nested in the body of the function change_person.
        The scope of these variables also includes the nested bodies of other function definitions that occur earlier.
        This allows these variables to be referenced by any functions, regardless of where they are defined in the module.
        The reply function, which calls change_person, might be defined before change_person in the doctor module.
"""