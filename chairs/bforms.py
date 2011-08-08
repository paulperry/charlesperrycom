# chairs/bforms.py

from google.appengine.ext.db import djangoforms
from django import forms
import models

class ChairForm(djangoforms.ModelForm):
    class Meta:
        model = models.Chair
        


