# chairs/models.py

from google.appengine.ext import db
from django import forms

class Chair(db.Model):
    name = db.StringProperty()
    material =  db.StringProperty()
#    year =  db.IntegerProperty()
    year =  db.StringProperty()
    image =  db.StringProperty()
    created_on = db.DateTimeProperty(auto_now_add = 1)
#    created_by = db.UserProperty()
    
    def __str__(self):        
        return '%s' %self.name
    
    def get_absolute_url(self):
        return '/chairs/%s/' % self.key()


   
    

