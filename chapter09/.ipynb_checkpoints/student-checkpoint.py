"""
Author: Le Tuan Luc
Date: 2021/09/29
Program: student.py
Problem:
    
Solution:
    >>>
"""
# class Marks(object):
#     def __init__(self, marks):
#         self.student_marks = []
    
#     def set_marks(self, marks):
#         self.student_marks.append(marks)

#     def get_marks(self):
#         return self.student_marks


class Student(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender