"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_08_page_133.py
Problem:
    Write a script named copyfile.py. This script should prompt the user for the names of two text files.
    The contents of the first file should be input and written to the second file.
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


def main():
    print('Input file')
    input_flie = open_text('r')
    print('Output file')
    output_file = open_text('a')
    output_file.write(input_flie.read())


if __name__ == "__main__":
    main()
