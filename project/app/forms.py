# from project.app.models import img_upload


from django import forms
from .models import img_upload
from tkinter import Image


class ImageFrom(forms.ModelForm):
    
    class Meta:
        model = img_upload
        fields = ("photo",)
        labels = {"photo":""}
