from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("instruction/", views.instruction, name="instruction"),
    path("generator/", views.generate_nonogram, name="generator"),
    path("puzzles/", views.puzzles_list, name="puzzles_list"),
    path("puzzles/<int:puzzle_id>/", views.puzzle_detail, name="puzzle_detail"),
]
