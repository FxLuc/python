"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_08_page_165.py
Problem:
    A file concordance tracks the unique words in a file and their frequencies.
    Write a program that displays a concordance for a file.
    The program should output the unique words and their frequencies in alphabetical order.
    Variations are to track sequences of two words and their frequencies, or n words and their frequencies.
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
    unique = {}
    word_list = file_contents.split()
    for word in word_list:
        if word not in unique:
            freq = unique.get(word, None)
            if freq == None:
                unique[word] = 1
            else:
                unique[word] = freq + 1
    word_list = list(unique.keys())
    word_list.sort()
    for word in word_list:
        print(word, unique[word])


def main():
    input_file = open_text('r')
    sorted_unique_file(input_file)


if __name__ == "__main__":
    main()
