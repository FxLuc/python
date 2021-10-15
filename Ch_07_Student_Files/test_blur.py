"""
File: test_blur.py
Tests a function process blur image
"""

from images import Image
from functools import reduce

def tripleSum(triple1, triple2):
    (r1, g1, b1) = triple1
    (r2, g2, b2) = triple2
    return (r1 + r2, g1 + g2, b1 + b2)

def convert_blur(image):
    """Converts the argument image to black and white."""
    for y in range(1, image.getHeight()-1):
        for x in range(1, image.getWidth()-1):
            oldP = image.getPixel(x, y)
            left = image.getPixel(x - 1, y)
            right = image.getPixel(x + 1, y)
            top = image.getPixel(x, y - 1)
            bottom = image.getPixel(x, y + 1)
            sums = reduce(tripleSum,[oldP, left, right, top, bottom])
            averages = tuple(map(lambda x: x // 5, sums))
            image.setPixel(x, y, averages)



def main(filename="smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue. ")
    image.draw()
    convert_blur(image)
    print("Close the image window to quit. ")
    image.draw()


if __name__ == '__main__':
    main()
