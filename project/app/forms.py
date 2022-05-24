# from project.app.models import img_upload


from django import forms
from .models import ImageUpload
from tkinter import Image


class ImageFrom(forms.ModelForm):
    
    class Meta:
        model = ImageUpload
        fields = ("photo",)
        labels = {"photo": ""}
