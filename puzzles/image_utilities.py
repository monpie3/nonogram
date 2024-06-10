import numpy as np
import rembg
from PIL import Image


def threshold(image: Image.Image, threshold: int) -> Image.Image:
    return image.point(lambda pixel: 0 if pixel > threshold else 255)


def resize_img(img: Image.Image, max_width: int) -> Image.Image:
    current_width = img.size[0]

    if current_width <= max_width:
        return img

    current_hight = img.size[1]
    wpercent = max_width / float(current_width)
    hsize = int(float(current_hight) * float(wpercent))

    return img.resize((max_width, hsize), Image.Resampling.LANCZOS)


def remove_empty_space(img):
    """
    Remove empty rows and columns from the image.
    """
    img = np.array(img, dtype=int)

    rows_to_delete = np.all(img == 1, axis=1)
    cols_to_delete = np.all(img == 1, axis=0)

    filtered_img = img[~rows_to_delete, :]
    filtered_img = filtered_img[:, ~cols_to_delete]

    return Image.fromarray((filtered_img * 255).astype(np.uint8))


def transform_img(img: Image.Image):
    """
    Transform the image by removing the background and converting it to binary.

    Args:
        img (Image.Image): The input image to be transformed.

    Returns:
        The transformed image with the background removed,
        and converted to binary.
    """
    img = rembg.remove(img)  # Remove the background
    img = threshold(img, threshold=10)
    img = img.convert("1")  # Convert the image to binary
    img = remove_empty_space(img)
    img = img.convert("1")
    return resize_img(img, max_width=15)
