# bio/bforms.py

from google.appengine.ext.db import djangoforms 
from django import forms
import models

class BioForm(djangoforms.ModelForm):
    class Meta:
        model = models.Bio

class ContactForm(forms.Form):
    name =    forms.CharField()
    email  =  forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)


class SubscribeForm(forms.Form):
    name =    forms.CharField()
    email  =  forms.EmailField()

