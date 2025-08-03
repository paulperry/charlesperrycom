# chairs/bforms.py

from django import forms
from . import models

class ChairForm(forms.ModelForm):
    class Meta:
        model = models.Chair
        fields = '__all__'
        


