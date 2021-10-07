"""
Author: Le Tuan Luc
Date: 2021/10/01
Program: IT19A2B_LeTuanLuc_49481_cau01.py
Problem: Cau 01: Viết hàm in các số nguyên tố trong khoảng từ 30 đến 200.
"""
from math import sqrt


def prime(number):
    if (number <= 1): return False
    for i in range(2, int(sqrt(number))+1):
        if (number%i == 0): return False
    return True


def main():
    n = 30
    while (n <= 200):
        if (prime(n)): print(n, end=" ")
        n = n+1


if __name__ == "__main__":
    main()