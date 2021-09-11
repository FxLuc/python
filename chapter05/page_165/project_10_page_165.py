"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_10_page_165.py
Problem:
    Conversations often shift focus to earlier topics.
    Modify the therapist program to support this capability.
    Add each patient input to a history list.
    Then, occasionally choose an element at random from this list, change persons, and prepend (add at the beginning) the qualifier “Earlier you said that” to this reply.
    Make sure that this option is triggered only after several exchanges have occurred.
Solution:
    >>>
"""
import random
history = []
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
replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "you":"I", "am":"are", "myself":"yourself", "was":"were", "your":"my", "yours":"mine"}


def reply(sentence):
    probability = random.randint(1, 4)
    if probability in (1,2):
        return random.choice(hedges)
    elif probability == 3 and len(history) > 3:
        return " Earlier you said that" + change_person(random.choice(history))
    else:
        history.append(sentence)
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