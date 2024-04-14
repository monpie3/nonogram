import logging

import numpy as np
from PIL import Image, ImageFilter


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
