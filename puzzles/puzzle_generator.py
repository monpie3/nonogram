import logging
from enum import Enum

import numpy as np
from PIL import Image, ImageFilter


class PixelColor(Enum):
    WHITE = 1
    BLACK = 0


def erode(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MinFilter(3))
    return image


def dilate(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(3))
    return image


def smooth(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.SMOOTH)
    return image


def count_black_pixels(image_array):
    row_counts = []

    for row in image_array:
        row_count = []
        num_of_black = 0

        for i, el in enumerate(row):
            if el == PixelColor.WHITE.value:
                if num_of_black > 0:
                    row_count.append(num_of_black)
                num_of_black = 0
            else:
                num_of_black += 1
                if i == len(row) - 1:  # if last element is black
                    row_count.append(num_of_black)
        row_counts.append(row_count)
    return row_counts


def convert_img_to_grid(image):
    image_array = np.array(image)
    row_counts = count_black_pixels(image_array)
    col_counts = count_black_pixels(image_array.T)

    return row_counts, col_counts


def generate_nonogram_from_image(image_path):
    logging.info("Generating nonogram from image: %s", image_path)

    # Load image
    img = Image.open(image_path)

    # Converting the image to grayscale, as edge detection
    # requires input image to be of mode = Grayscale (L)
    img = img.convert("L")

    # You can obtain a better outcome by applying the ImageFilter.SMOOTH filter
    # Before finding the edges
    img = smooth(5, img)

    # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
    img = img.filter(ImageFilter.FIND_EDGES)

    # Saving the Image
    img.save("static/images/1_img_edges.jpg")

    threshold = 20  # Threshold for edge detection

    # Threshold
    img = img.point(lambda p: 255 if p < threshold else 0)

    # Convert the image to binary
    img = img.convert("1")

    img = erode(3, img)
    img = dilate(1, img)

    return "static/images/temp_edges.jpg"
