from cloudinary.models import CloudinaryField
from django.db import models
from PIL import Image

from . import image_utilities

DIFFICULTY_CHOICES = [
    (1, "★"),
    (2, "★★"),
    (3, "★★★"),
    (4, "★★★★"),
    (5, "★★★★★"),
]


class Nonogram(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField("image")
    puzzle_data = models.JSONField()
    puzzle_solution = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    difficulty_level = models.IntegerField(choices=DIFFICULTY_CHOICES, default=3)
    author = models.CharField(max_length=100, default="Anonymous")

    def __str__(self):
        return f"{self.title} {self.difficulty_level}"
