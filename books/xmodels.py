# books/models.py

from google.appengine.ext import db
from django import forms

class Book(db.Model):
    def __str__(self):        
        return '%s' %self.name
    
    def get_absolute_url(self):
        return '/books/%s/' % self.key()


   
    

