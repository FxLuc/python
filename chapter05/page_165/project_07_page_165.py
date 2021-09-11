"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_07_page_165.py
Problem:
    Write a program that inputs a text file.
    The program should print the unique words in the file in alphabetical order.
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


def sorted_unique_file(input_file):
    file_contents = input_file.read()
    unique = []
    word_list = file_contents.split()
    for word in word_list:
        if word not in unique:
            unique.append(word)
    print("\n".join(sorted(list(set(unique)))))


def main():
    input_file = open_text('r')
    sorted_unique_file(input_file)


if __name__ == "__main__":
    main()
