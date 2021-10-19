"""
Author: Le Tuan Luc
Date: 2021/10/09
Program: IT19A2B_LeTuanLuc_49481_cau02.py
"""
students = []


class Student:
    def __init__(self, _id, _name, _tel, _theory_marks, _practice_marks) -> None:
        self.id = _id
        self.name = _name
        self.tel = _tel
        self.theory_marks = float(_theory_marks)
        self.practice_marks = float(_practice_marks)
    @property
    def overall(self):
        return float(f"{(self.theory_marks + self.practice_marks)/2: .2f}")
    @property
    def classification(self):
        if (self.overall < 5.0):
            return "F"
        elif (self.overall < 7.0):
            return "D"
        elif (self.overall < 8.0):
            return "C"
        elif (self.overall < 9.0):
            return "B"
        else:
            return "A"


def is_students_empty():
    if students == []:
        print("You must import data from file input.txt first!")
        return True
    return False


def import_files():
    print("Importing from file input...")
    f = open("IT19A2B_LeTuanLuc_49481_inp.txt", 'r')
    for line in f:
        data_in_line = line.split("|")
        students.append(Student(data_in_line[0], data_in_line[1], data_in_line[2], data_in_line[3], data_in_line[4]))
    print("Done!")


def show_data():
    if not is_students_empty():
        print("{:^7} {:<20} {:^10} {:^10} {:^10} {:^10} {:^15}".format("ID", "Name", "Tel", "Theory", "Pratice", "Final", "Classification"))
        for student in students:
            print("{:^7} {:<20} {:^10} {:^10} {:^10} {:^10} {:^15}".format(student.id, student.name, student.tel, student.theory_marks, student.practice_marks, student.overall, student.classification))

def filter_students_overall(overall):
    if not is_students_empty():
        print("Creating file output...")
        f = open("IT19A2B_LeTuanLuc_49481_out.txt", "a")
        print("Exporting to file output...")
        for student in students:
            if student.overall >= overall:
                f.write(f"{student.id}|{student.name}|{student.tel}|{student.theory_marks}|{student.practice_marks}|{student.overall}|{student.classification}\n")
        print("Done!")


def main():
    print("\n", "="*5, " MENU ", "="*5)
    print("1. Import data from file input.txt")
    print("2. Show data")
    print("3. Export students have final grade > 7 to output.txt")
    print("Enter any number else to quit.")
    choice = input("Your choice: ")
    print()
    try:
        choice = int(choice)
        if choice == 1:
            import_files()
        if choice == 2:
            show_data()
        if choice == 3:
            filter_students_overall(7)
        if choice > 3:
            quit()
        main()
    except ValueError:
        print("Enter a positive number!")
        main()



if __name__ == "__main__":
    main()