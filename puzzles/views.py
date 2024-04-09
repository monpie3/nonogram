from django.shortcuts import redirect, render

from puzzles.forms import NonogramForm
from puzzles.models import Nonogram
from puzzles.puzzle_generator import generate_nonogram_from_image


def index(request):
    return render(request, "puzzles/index.html")


def instruction(request):
    return render(request, "puzzles/instruction.html")


def generate_nonogram(request):
    if request.method == "POST":
        form = NonogramForm(request.POST, request.FILES)
        if form.is_valid():
            image_path = form.cleaned_data["image"]
            nonogram_instance = generate_nonogram_from_image(image_path)
            return redirect("puzzles/puzzle_detail.html", pk=nonogram_instance.pk)
    else:
        form = NonogramForm()

    return render(request, "puzzles/puzzle_generator.html", {"form": form})


def puzzles_list(request):
    nonograms = Nonogram.objects.all()
    return render(request, "puzzles/puzzles_list.html", {"nonograms": nonograms})


def puzzle_detail(request, nonogram_id):
    nonogram = Nonogram.objects.get(id=nonogram_id)
    return render(request, "puzzles/puzzle_detail.html", {"nonogram": nonogram})
