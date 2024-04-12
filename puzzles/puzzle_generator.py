import logging

import numpy as np
from PIL import Image, ImageFilter


def generate_nonogram_from_image(image_path):
    logging.info("Generating nonogram from image: %s", image_path)

    # Load image
    img = Image.open(image_path)

    # Converting the image to grayscale, as edge detection
    # requires input image to be of mode = Grayscale (L)
    img = img.convert("L")

    # You can obtain a better outcome by applying the ImageFilter.SMOOTH filter
    # Before finding the edges
    img = img.filter(ImageFilter.SMOOTH)

    # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
    img = img.filter(ImageFilter.FIND_EDGES)

    # Saving the Image
    img.save("static/images/img_edges.jpg")

    img_array = np.array(img)

    nonogram = np.zerod(img_array.shape, dtype=np.uint8)
    threshold = 20  # Threshold for edge detection

    for y in range(img_array.shape[0]):
        for x in range(img_array.shape[1]):
            if img_array[y, x] < threshold:
                nonogram[y, x] = 0
            else:
                nonogram[y, x] = 255

    Image.fromarray(nonogram).save("static/images/nonogram.jpg")

    return "static/images/temp_edges.jpg"
