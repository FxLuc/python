"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_04_page_165.py
Problem:
    Make the following modifications to the original sentence-generator program:
    a. The prepositional phrase is optional. (It can appear with a certain probability.)
    b. A conjunction and a second independent clause are optional: The boy took a drink and the girl played baseball.
    c. An adjective is optional: The girl kicked the red ball with a sore foot.
    You should add new variables for the sets of adjectives and conjunctions.
Solution:
    >>>
"""
import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
adjectives = ("RED", "LITTLE")
conjunctions = ("AND", "BUT")


def sentence():
    first = independent_clause()
    if random.randint(1, 5) == 1:
        return first + " " + random.choice(conjunctions) + \
            " " + independent_clause()
    else:
        return first


def independent_clause():
    return noun_phrase() + " " + verd_phrase()


def noun_phrase():
    if random.randint(1, 2) == 1:
        adj = random.choice(adjectives) + " "
    else:
        adj = " "
    return random.choice(articles) + " " + adj + random.choice(nouns)


def verd_phrase():
    if random.randint(1, 3) == 1:
        prep_phrase = " " + prepositional_phrase()
    else:
        prep_phrase = ""
    return random.choice(verbs) + " " + noun_phrase() + prep_phrase


def prepositional_phrase():
    return random.choice(prepositions) + " " + noun_phrase()


def main():
    number = int(input("Enter the number of sentence :"))
    for count in range(number):
        print(sentence())


# The entry point for program execution
if __name__ == "__main__":
    main()
