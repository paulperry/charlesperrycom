# bio/bforms.py

from django import forms
from . import models

class BioForm(forms.ModelForm):
    class Meta:
        model = models.Bio
        fields = '__all__'

class ContactForm(forms.Form):
    name =    forms.CharField()
    email  =  forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)


class SubscribeForm(forms.Form):
    name =    forms.CharField()
    email  =  forms.EmailField()

