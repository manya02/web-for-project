from asyncio.windows_events import NULL
from pyexpat import model
from unicodedata import name
from django.db import models

class Contact (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    ship=models.TextField()
    pro=models.CharField(max_length=2,default="P1")

    def __str__(self):
        return self.name


class img_upload(models.Model):
    photo = models.ImageField(upload_to="my_img")
    

# Create your models here.
