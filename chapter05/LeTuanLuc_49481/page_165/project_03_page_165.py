"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_03_page_165.py
Problem:
    Write a program that allows the user to navigate the lines of text in a file.
    The program should prompt the user for a filename and input the lines of text into a list.
    The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number.
    Actual line numbers range from 1 to the number of lines in the file.
    If the input is 0, the program quits. Otherwise, the program prints the line associated with that number.
Solution:
    >>>
"""
import random


def get_words(file_name):
    input_file = open(file_name, 'r')
    words = []
    for line in input_file:
        words.extend(line.split())
    return tuple(words)


articles = get_words("project_03_dict/articles.txt")
nouns = get_words("project_03_dict/nouns.txt")
verbs = get_words("project_03_dict/verbs.txt")
prepositions = get_words("project_03_dict/prepositions.txt")


def noun_phrase():
    return random.choice(articles) + " " + random.choice(nouns)


def prepositional_phrase():
    return random.choice(prepositions) + " " + noun_phrase()


def verb_phrase():
    return random.choice(verbs) + " " + noun_phrase() + " " + prepositional_phrase()


def sentence():
    return noun_phrase() + " " + verb_phrase()


def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


# The entry point for program execution
if __name__ == "__main__":
    main()
