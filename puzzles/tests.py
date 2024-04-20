import numpy as np
from django.test import TestCase

from puzzles import puzzle_generator


class TestTransformImg(TestCase):
    def test_transform_img(self):
        image_array = np.array(
            [
                [0, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 1, 1, 1, 0],
                [0, 0, 1, 1, 0, 1, 1, 1],
                [1, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1, 0, 0, 1],
            ]
        )

        expected_row_counts = [[3, 2], [3, 1], [2, 1], [5], [1, 1], [1, 2]]
        expected_col_counts = [
            [1, 1],
            [3, 1],
            [2, 1],
            [1, 1, 1],
            [3],
            [1, 1],
            [1, 1, 1],
            [2],
        ]

        row_counts, col_counts = puzzle_generator.convert_img_to_grid(image_array)

        assert row_counts == expected_row_counts
        assert col_counts == expected_col_counts
