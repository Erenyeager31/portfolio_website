from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=122)
    url = models.CharField(max_length=122)
    stack = models.CharField(max_length=122,default='-')
    desc = models.TextField(default='-')

    def __str__(self):
        return self.name
    
