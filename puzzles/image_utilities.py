from PIL import Image, ImageFilter


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
