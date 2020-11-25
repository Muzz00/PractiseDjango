from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=256)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
     

class Group(models.Model):
    """
    docstring
    """
    links = models.ManyToManyField(Link)
    hashID = models.CharField(max_length=200)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    