from enum import Enum
from io import BytesIO

import numpy as np
import requests
from PIL import Image
from rest_framework import status

from puzzles.forms import NonogramForm
from puzzles.models import Nonogram

from . import image_utilities


class PixelColor(Enum):
    WHITE = 1
    BLACK = 0


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


def convert_img_to_clues(img: Image.Image):
    """
    Grup the black pixels in the image to form the nonogram data.
    """
    img_array = np.array(img)
    row_clues = count_black_pixels(img_array)
    col_clues = count_black_pixels(img_array.T)

    return row_clues, col_clues


def generate_nonogram_from_form(form: NonogramForm) -> Nonogram:
    """
    Generate nonogram data from an image and save it in the database.

    Args:
        form (NonogramForm): The form containing the image.

    Returns:
        Nonogram: The Nonogram instance with generated data.
    """
    img = form.cleaned_data["image"]

    # Load image
    # TO DO: use the Cloudinary API to upload the image
    response = requests.get(img.url, timeout=10)
    if response.status_code == status.HTTP_200_OK:
        img = Image.open(BytesIO(response.content))
    else:
        raise Exception("Cannot download the image")

    # Resize image
    # TO DO: use the Cloudinary resizing transformations
    img = image_utilities.resize_img(img, max_width=10)

    # Transform the image
    img = image_utilities.transform_img(img)

    # Create nonogram data
    row_clues, col_clues = convert_img_to_clues(img)

    nonogram_data = {"row_clues": row_clues, "col_clues": col_clues}

    # Create a new Nonogram instance, but don't save the instance yet
    nonogram_instance = form.save(commit=False)
    # Modify nonogram data field
    nonogram_instance.puzzle_data = nonogram_data
    nonogram_instance.puzzle_solution = np.array(img, dtype=int).tolist()
    # Save the instance
    nonogram_instance.save()

    return nonogram_instance
