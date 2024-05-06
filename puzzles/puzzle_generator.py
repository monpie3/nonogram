from enum import Enum

import numpy as np
from PIL import Image, ImageFilter

from puzzles.models import Nonogram


class PixelColor(Enum):
    WHITE = 1
    BLACK = 0


def erode(image: Image.Image, cycles: int) -> Image.Image:
    for _ in range(cycles):
        image = image.filter(ImageFilter.MinFilter(3))
    return image


def dilate(image: Image.Image, cycles: int) -> Image.Image:
    for _ in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(3))
    return image


def smooth(image: Image.Image, cycles: int) -> Image.Image:
    for _ in range(cycles):
        image = image.filter(ImageFilter.SMOOTH)
    return image


def threshold(image: Image.Image, threshold: int) -> Image.Image:
    return image.point(lambda pixel: 0 if pixel > threshold else 255)


def count_black_pixels(image_array: np.ndarray) -> list[list[int]]:
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


def resize_img(img: Image.Image, max_width: int) -> Image.Image:
    current_width = img.size[0]

    if current_width <= max_width:
        return img

    current_hight = img.size[1]
    wpercent = max_width / float(current_width)
    hsize = int(float(current_hight) * float(wpercent))
    return img.resize((max_width, hsize), Image.Resampling.LANCZOS)


def transform_img(img: Image.Image) -> Image.Image:
    """
    Transform the image to a binary image with edges detected.
    """
    # Converting the image to grayscale, as edge detection
    # requires input image to be of mode = Grayscale (L)
    img = img.convert("L")

    # You can obtain a better outcome by applying the ImageFilter.SMOOTH filter
    # Before finding the edges
    img = smooth(img, cycles=5)

    # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
    img = img.filter(ImageFilter.FIND_EDGES)

    # Threshold
    img = threshold(img, threshold=20)

    # Convert the image to binary
    img = img.convert("1")

    img = erode(img, cycles=3)
    return dilate(img, cycles=1)


def convert_img_to_grid(img: Image.Image):
    """
    Grup the black pixels in the image to form the nonogram data.
    """
    img_array = np.array(img)
    row_counts = count_black_pixels(img_array)
    col_counts = count_black_pixels(img_array.T)

    return row_counts, col_counts


def generate_nonogram_from_image(img_path: str) -> Nonogram:
    """
    Generate nonogram data from an image and save it in the database.

    Args:
        image_path (str): The path to the image file.

    Returns:
        Nonogram: The Nonogram instance with generated data.
    """

    # Load image
    img = Image.open(img_path)

    # Resize image
    img = resize_img(img, max_width=100)

    # Transform the image
    img = transform_img(img)

    # Create nonogram data
    row_counts, col_counts = convert_img_to_grid(img)

    nonogram_data = {"rows": row_counts, "columns": col_counts}

    # Create a new Nonogram instance
    nonogram_instance = Nonogram()
    # Set the nonogram data and save the Nonogram instance
    nonogram_instance.puzzle_data = nonogram_data
    nonogram_instance.save()

    return nonogram_instance
