# jewelry/models.py

from django.db import models

class Jewelry(models.Model):
    name = models.CharField(max_length=200)
    material = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    style = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    prev = models.CharField(max_length=200, blank=True)
    next = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Jewelry"
    
    def __str__(self):        
        return self.name or str(self.pk)
    
    def get_absolute_url(self):
        return f'/jewelry/{self.pk}'


   
    

