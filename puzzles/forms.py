# forms.py

from django import forms

from .models import Nonogram


class NonogramForm(forms.ModelForm):
    class Meta:
        model = Nonogram
        fields = ["title", "image"]
