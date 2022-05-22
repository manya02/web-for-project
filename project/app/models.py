from unicodedata import name
from django.db import models

class Contact (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    ship=models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
