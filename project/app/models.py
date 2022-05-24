from django.db import models


class Contact (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    ship = models.TextField()
    pro = models.CharField(max_length=2,default="P1")

    def __str__(self):
        return self.name


class ImageUpload(models.Model):
    photo = models.ImageField(upload_to="images")


# Create your models here.
