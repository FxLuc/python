"""
Author: Le Tuan Luc
Date: 2021/08/11
Program: casestudy_nondirective_sychotherapys_page_159.py
Problem:
    Write a program that emulates a nondirective psychotherapist.
Solution:
    Conducts an interactive session of nondirective psychotherapy.
"""
import random

hedges = (
    "Please tell me more.",
    "Many of my patients tell me the same thing.",
    "Please continue."
    )
qualifiers = (
    "Why do you say that ",
    "You seem to think that ",
    "Can you explain why "
    )
replacements = {
    "I": "you",
    "me": "you",
    "my": "your",
    "we": "you",
    "us": "you",
    "mine": "yours"
    }


def reply(sentence):
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + change_person(sentence)


def change_person(sentence):
    words = sentence.split()
    reply_words = []
    for word in words:
        reply_words.append(replacements.get(word, word))
    return " ".join(reply_words)


def main():
    print("Good morning, I hope you are well today.\nWhat can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))


# The entry point for program execution
if __name__ == "__main__":
    main()
