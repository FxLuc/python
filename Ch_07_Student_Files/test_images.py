"""

Test images script
"""
from images import Image


def draw_image():
    image = Image(150, 150)
    image.draw()
    blue = (0, 0, 255)
    y = image.getHeight() // 2
    for x in range(image.getWidth()):
        image.setPixel(x, y - 1, blue)
        image.setPixel(x, y, blue)
        image.setPixel(x, y + 1, blue)
    image.draw()
    image.save("horizontal.gif")


if __name__ == '__main__':
    image = Image("smokey.gif")
    image.draw()
    image.getPixel(0, 0)

    draw_image()
