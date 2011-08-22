# books/bforms.py

from google.appengine.ext.db import djangoforms
from django import forms
import models

class BookForm(djangoforms.ModelForm):
    class Meta:
        model = models.Book
        


