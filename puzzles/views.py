from django.shortcuts import get_object_or_404, redirect, render

from puzzles.forms import NonogramForm
from puzzles.models import Nonogram
from puzzles.puzzle_generator import generate_nonogram_from_form


def index(request):
    return render(request, "puzzles/index.html")


def instruction(request):
    return render(request, "puzzles/instruction.html")


def generate_nonogram(request):
    if request.method == "POST":
        form = NonogramForm(request.POST, request.FILES)
        if form.is_valid():
            nonogram_instance = generate_nonogram_from_form(form)
            return redirect("puzzle_detail", puzzle_id=nonogram_instance.pk)
    else:
        form = NonogramForm()

    return render(request, "puzzles/puzzle_generator.html", {"form": form})


def puzzles_list(request):
    nonograms = Nonogram.objects.all().values("id", "title")
    return render(request, "puzzles/puzzles_list.html", {"nonograms": nonograms})


def puzzle_detail(request, puzzle_id):
    nonogram = get_object_or_404(Nonogram, id=puzzle_id)
    return render(request, "puzzles/puzzle_detail.html", {"nonogram": nonogram})
