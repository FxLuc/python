"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: casestudy_generating_sentences_page_150.py
Problem:
    Write a program that generates sentences.
Solution:
    Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.
"""
import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

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
