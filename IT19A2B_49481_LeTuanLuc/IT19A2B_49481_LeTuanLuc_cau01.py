"""
Author: Le Tuan Luc
Date: 2021/10/17
Program: IT19A2B_49481_LeTuanLuc_cau01.py
Question 01: Viết hàm in các số nguyên tố trong khoảng từ 10 đến 100.
"""
from math import sqrt


# check prime
def is_prime(number):
    if (number <= 1): return False
    for i in range(2, int(sqrt(number))+1):
        if (number%i == 0): return False
    return True


def main():
    number_from = 10
    number_to = 100
    # loop from 10 to 100
    while (number_from <= number_to):
        if (is_prime(number_from)): print(number_from, end=" ")
        number_from += 1


if __name__ == "__main__":
    main()