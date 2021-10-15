"""
File: foursquares.py

Draws squares in the corners of a turtle window.
One square is black, another is gray, and the
remaining two are in random colors.
"""

import random
from turtle import Turtle


def drawSquare(turtle, x, y, length):
    turtle.up()
    turtle.move(x, y)
    turtle.setDirection(270)
    turtle.down()
    for count in range(4):
        turtle.move(length)
        turtle.turn(90)


def main():
    turtle = Turtle()
    # turtle.setWidth(1)
    # Length of square
    length = 40
    # Relative distances to corners from origin
    width = turtle.getWidth() / 2
    height = turtle.getHeight() / 2
    # Black
    turtle.setColor(0, 0, 0)
    # Upper left corner
    drawSquare(turtle, -width, height, length)
    # Gray
    turtle.setColor(127, 127, 127)
    # Lower left corner
    drawSquare(turtle, -width, length - height, length)
    # First random color
    turtle.setColor(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
    # Upper right corner
    drawSquare(turtle, width - length, height, length)
    # Second random color
    turtle.setColor(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255))
    # Lower right corner
    drawSquare(turtle, width - length,
               length - height, length)


if __name__ == '__main__':
    main()
