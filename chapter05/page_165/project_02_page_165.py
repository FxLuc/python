"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_02_page_165.py
Problem:
    Write a program that allows the user to navigate the lines of text in a file.
    The program should prompt the user for a filename and input the lines of text into a list.
    The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number.
    Actual line numbers range from 1 to the number of lines in the file.
    If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.
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
            return open_text(mode)
        else:
            quit()
    return open(file_name, mode)


def text_line_to_list(input_file):
    data = []
    for line in input_file:
        data.append(line)
    return data


def line_number(data):
    if len(data) == 0:
        quit()
    line = int(input("Enter for a line number: "))
    if line == 0:
        quit()
    elif line > len(data):
        print(f"Error: The number must be <= {len(data)}")
        return line_number(data)
    return line


def main():
    input_file = open_text('r')
    data = text_line_to_list(input_file)
    actual_line = line_number(data) - 1
    print(data[actual_line])


if __name__ == "__main__":
    main()
