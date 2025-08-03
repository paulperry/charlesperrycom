# jewelry/bforms.py

from django import forms
from . import models

class JewelryForm(forms.ModelForm):
    class Meta:
        model = models.Jewelry
        fields = '__all__'
        


