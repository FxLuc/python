"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: project_10_page_133.py
Problem:
    Write a script named dif.py. This script should prompt the user for the names of two text files and compare the contents of the two files to see if they are the same.
    If they are, the script should simply output "Yes". If they are not, the script should output "No", followed by the first lines of each file that differ from each other.
    The input loop should read and compare lines from each file. The loop should break as soon as a pair of different lines is found.
Solution:
    >>>
"""
from os.path import exists


def open_text(mode):
    file_name = input("Enter a file name: ")
    if not exists(file_name):
        print("Error: the file does not exist!")
        is_try_again = input("Try again? (y/n)")
        if is_try_again == "y" or is_try_again == "yes":
            open_text(mode)
        else:
            quit()
    return open(file_name, mode)


def is_compare(input_flie_a, input_flie_b):
    for line_a in input_flie_a:
        if line_a != input_flie_b.readline():
            return False
    return True


def main():
    print('Input file A')
    input_flie_a = open_text('r')
    print('Input file B')
    input_flie_b = open_text('r')
    print(is_compare(input_flie_a, input_flie_b))


if __name__ == "__main__":
    main()
