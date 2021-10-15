from turtle import Turtle


def drawPolygon(turtle, vertices):
    """Draws a polygon from a list of vertices.
    The list has the form [(x1, y1), ..., (xn, yn)]."""
    turtle.up()
    (x, y) = vertices[-1]
    turtle.move(x, y)
    turtle.down()
    for (x, y) in vertices:
        turtle.move(x, y)


def main():
    turtle = Turtle()
    drawPolygon(turtle, [(20, 20), (-20, 20), (-20, -20)])


main()
