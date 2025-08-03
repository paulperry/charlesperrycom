# bio/models.py

from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/bio/{self.pk}/'
    


    
    
