"""
Author: Le Tuan Luc
Date: 2021/09/10
Program: convert_image.py
Problem:
    Develop three algorithms for lightening, darkening, and color filtering. 
Solution:
    >>>
"""
from PIL import Image


def color_filter(image_path, amount):
    image = Image.open(image_path)
    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))
            image.putpixel((x, y), color_filtering((r, g, b), amount))
    image.show()


def color_filtering(pixel, amount):
    r = int(int(pixel[0]) + int(pixel[0]) * int(amount[0])/100)
    g = int(int(pixel[1]) + int(pixel[1]) * int(amount[1])/100)
    b = int(int(pixel[2]) + int(pixel[2]) * int(amount[2])/100)
    new_pixel = rgb_limiting(r, g, b)
    return new_pixel


def change_brightness(image_path, amount):
    image = Image.open(image_path)
    amount = amount / 100
    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))
            image.putpixel((x, y), changing_brightness((r, g, b), amount))
    image.show()

def changing_brightness(pixel, amount):
    r = int(int(pixel[0]) + int(pixel[0]) * amount)
    g = int(int(pixel[1]) + int(pixel[1]) * amount)
    b = int(int(pixel[2]) + int(pixel[2]) * amount)
    new_pixel = rgb_limiting(r, g, b)
    return new_pixel

def rgb_limiting(r, g, b):
    MAX_LIM = 255
    if r > MAX_LIM: r = MAX_LIM
    if g > MAX_LIM: g = MAX_LIM
    if b > MAX_LIM: b = MAX_LIM
    MIN_LIM = 0
    if r < MIN_LIM: r = MIN_LIM
    if g < MIN_LIM: g = MIN_LIM
    if b < MIN_LIM: b = MIN_LIM
    return (r, g, b)


def main():
    image_path = "chapter07/convert_image/smokey.jpg"
    change_brightness(image_path, 200) #lighten 200%
    change_brightness(image_path, -50) #darken 50%
    color_filter(image_path, (100, 100, 0)) #filter 100% yellow
    color_filter(image_path, (0, 0, 50)) #filter 50% blue

if __name__ == "__main__":
    main()