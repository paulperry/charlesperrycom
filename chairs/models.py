# chairs/models.py

from django.db import models

class Chair(models.Model):
    name = models.CharField(max_length=200)
    material = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=10, blank=True)
    image = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/chairs/{self.pk}/'


   
    

