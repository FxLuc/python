"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_09_page_165.py
Problem:
    In Case Study 5.5, when the patient addresses the therapist personally, the therapist’s reply does not change persons appropriately.
    To see an example of this problem, test the program with “you are not a helpful therapist.”
    Fix this problem by repairing the dictionary of replacements.
Solution:
    >>>
"""
import random

hedges = (
    "Please tell me more.",
    "Many of my patients tell me the same thing.",
    "Please continue."
)
qualifiers = (
    "Why do you say that?",
    "You seem to think that?",
    "Can you explain why? "
    "Earlier you said that."
)
replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours",
                "you": "I", "am": "are", "myself": "yourself", "was": "were", "your": "my", "yours": "mine"}


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
        if sentence.upper() == "YOU ARE NOT A HELPFUL THERAPIST":
            print("I'm so sorry about that.")
            break
        print(reply(sentence))


# The entry point for program execution
if __name__ == "__main__":
    main()
