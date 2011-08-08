from google.appengine.ext import db
#from django import newforms as forms

class Sculpture(db.Model):
#    year =  db.IntegerProperty()
    year =  db.StringProperty()
    name = db.StringProperty()
    location = db.StringProperty()
    address =  db.StringProperty()
    city =  db.StringProperty()
    state =  db.StringProperty()
    country =  db.StringProperty()
    material =  db.StringProperty()
    size =  db.StringProperty()
    style =  db.StringProperty(required=True, choices=['planar','topological','ribbed','solid'])
    image =  db.StringProperty()
#    geopt = GeoPtProperty()
    lat =  db.StringProperty()
    lon =  db.StringProperty()
    geolink = db.StringProperty()
#    geolink = db.LinkProperty()
    visible = db.StringProperty() # geo link has visible sculpture in it
#    created_on = db.DateTimeProperty(auto_now_add = 1)
#    created_by = db.UserProperty()
    prev_style = db.StringProperty()
    next_style = db.StringProperty()
    prev_material = db.StringProperty()
    next_material = db.StringProperty()

    def __str__(self):        
        return '%s' %self.key().id_or_name()
    
    def get_absolute_url(self):
        return '/sculpture/%s' % str(self)


   
    

