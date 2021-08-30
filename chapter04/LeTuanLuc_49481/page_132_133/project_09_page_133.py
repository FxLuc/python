"""
Author: Le Tuan Luc
Date: 2021/08/30
Program: project_09_page_133.py
Problem:
    Write a script named numberlines.py. This script creates a program listing from a source program.
    This script should prompt the user for the names of two files.
    The input filename could be the name of the script itself, but be careful to use a different output filename!
    The script copies the lines of text from the input file to the output file, numbering each line as it goes.
    The line numbers should be right-justified in 4 columns, so that the format of a line in the output file looks like this example:
    1> This is the first line of text.
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
    input_file = open_text('r')
    print('Output file')
    output_file = open_text('a')
    count = 0
    for line in input_file:
        count += 1
        output_file.write(f"{count}> {line}")


if __name__ == "__main__":
    main()
