# puzzles/bforms.py

#from google.appengine.ext.db import djangoforms
import djangoforms
from django import forms
import models

class PuzzlesForm(djangoforms.ModelForm):
    class Meta:
        model = models.Jewelry
        


