from django.shortcuts import render


def index(request):
    return render(request, "puzzles/index.html")


def instruction(request):
    return render(request, "puzzles/instruction.html")
