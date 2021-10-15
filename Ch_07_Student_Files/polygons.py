"""

Draw polygon library
"""

from turtle import Turtle


def square(t, length):
    """Draws a square with the given length."""
    for count in range(4):
        t.forward(length)
        t.left(90)


def hexagon(t, length):
    """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(length)
        t.left(60)


def radialHexagons(t, n, length):
    """Draws a radial pattern of n hexagons with the given length."""
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)


def radialpattern(t, n, length, shape):
    """Draws a radial pattern of n shapes with the given length."""
    for count in range(n):
        shape(t, length)
        t.left(360 / n)


def test01():
    """ """
    t = Turtle()
    radialpattern(t, n=10, length=50, shape=square)
    t.clear()
    radialpattern(t, n=13, length=50, shape=hexagon)


if __name__ == '__main__':
    t = Turtle()
    #t.pencolor("blue")
    t.pencolor(225,225,0)
    t.hideturtle()
    square(t, 50)
    hexagon(t, 50)
    t.clear()
    radialHexagons(t, 10, 50)
    test01()

