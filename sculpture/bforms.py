# art/bforms.py 

from django import forms
from . import models

class SculptureForm(forms.ModelForm):
    class Meta:
        model = models.Sculpture
        exclude = ['created_on', 'prev_style', 'next_style', 'prev_material', 'next_material']
        


