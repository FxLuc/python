"""
Author: Le Tuan Luc
Date: 2021/08/29
Program: project_05_page_132.py
Problem:
    Define two scripts, shiftLeft.py and shiftRight.py, that expect a bit string as an input.
Solution:
    >>>
"""


def shift_left(bit_string, places):
    return bit_string[places:] + bit_string[0:places]


def shift_right(bit_string, places):
    return bit_string[-places:] + bit_string[0:-places]


def main():
    bit_string = input("Enter a bit string: ")
    places = int(input("Enter number place: "))
    print(shift_left(bit_string, places))
    print(shift_right(bit_string, places))


if __name__ == "__main__":
    main()
