# puzzles/bforms.py

from django import forms
from . import models

class PuzzleForm(forms.ModelForm):
    class Meta:
        model = models.Puzzle
        fields = '__all__'
        


