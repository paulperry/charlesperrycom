# jewelry/bforms.py

from google.appengine.ext.db import djangoforms
from django import forms
import models

class JewelryForm(djangoforms.ModelForm):
    class Meta:
        model = models.Jewelry
        


