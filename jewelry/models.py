# jewelry/models.py

from google.appengine.ext import db
from django import forms

class Jewelry(db.Model):
    name = db.StringProperty()
    material = db.StringProperty()
    size = db.StringProperty()
    style = db.StringProperty()
    image = db.StringProperty()
#    created_on = db.DateTimeProperty(auto_now_add = 1)
    prev = db.StringProperty()
    next = db.StringProperty()
    
    def __str__(self):        
        return '%s' %self.key().id_or_name()
    
    def get_absolute_url(self):
        return '/jewelry/%s' % str(self)


   
    

