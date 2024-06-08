# forms.py

from cloudinary.forms import CloudinaryFileField
from django import forms

from .models import Nonogram


class NonogramForm(forms.ModelForm):
    image = CloudinaryFileField()

    class Meta:
        model = Nonogram
        fields = ["title", "image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].options = {
            "width": 300,
        }
