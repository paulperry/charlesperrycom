# art/bforms.py 

from google.appengine.ext.db import djangoforms
from django import forms
import models

class SculptureForm(djangoforms.ModelForm):
    class Meta:
        model = models.Sculpture
        exclude = ['created_by']
        


