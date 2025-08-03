from django.db import models

class Sculpture(models.Model):
    STYLE_CHOICES = [
        ('planar', 'Planar'),
        ('topological', 'Topological'),
        ('ribbed', 'Ribbed'),
        ('solid', 'Solid'),
    ]
    
    year = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    material = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    style = models.CharField(max_length=20, choices=STYLE_CHOICES)
    image = models.CharField(max_length=200, blank=True)
    lat = models.CharField(max_length=20, blank=True)
    lon = models.CharField(max_length=20, blank=True)
    geolink = models.URLField(blank=True)
    visible = models.CharField(max_length=1, blank=True, default='y')
    prev_style = models.CharField(max_length=200, blank=True)
    next_style = models.CharField(max_length=200, blank=True)
    prev_material = models.CharField(max_length=200, blank=True)
    next_material = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name or str(self.pk)
    
    def get_absolute_url(self):
        return f'/sculpture/{self.pk}'


   
    

