# bio/models.py

from google.appengine.ext import db
from django import forms

class Bio(db.Model):
    name = db.StringProperty()
    
    def __str__(self):
        return '%s' %self.name
    
    def get_absolute_url(self):
        return '/poll/%s/' % self.key()
    


    
    
