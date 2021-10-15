"""
File: randomwalk.py

A turtle takes a random walk.
"""

import random
from turtle import Turtle


def randomWalk(t, turns, distance=20):
    for x in range(turns):
        if x % 2 == 0:
            t.left(random.randint(0, 270))
        else:
            t.right(random.randint(0, 270))
            t.forward(distance)


def main():
    t = Turtle()
    t.shape("turtle")
    randomWalk(t, 40, 30)


if __name__ == "__main__":
    main()
