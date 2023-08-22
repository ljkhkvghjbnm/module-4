# from django import forms
#
# class AdverisementForm(forms.Form):
#     title=forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(attrs={'class':"forms-control form-control-lg"})
#
#     )
#     description= forms.CharField(
#         widget=forms.Textarea(attrs={'class':"forms-control form-control-lg"})
#     )
#     price= forms.DecimalField(
#         widget=forms.NumberInput(attrs={'class':"forms-control form-control-lg"})
#     )
#     auction=forms.BooleanField(
#         widget=forms.CheckboxInput(attrs={'class':"font-check-input"})
#     )
#     image=forms.ImageField(
#         widget=forms.FileInput(attrs={'class':"forms-control form-control-lg"})
#     )

from django.forms import ModelForm
from django.db import models
from django.core.exceptions import ValidationError
import re

class Author(models.Model):

    title = models.CharField(max_length=3)

    description = models.TextField(max_length=3)

    price=models.DecimalField(max_digits=4,decimal_places=3)

    auction=models.BooleanField()

    image=models.ImageField()

class AdvertisementForm(ModelForm):
    class Meta:
        model = Author
        # fields = ['title','description','price','auction','image']
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0]=='?':
            raise ValidationError("Назвние не должно начинаться с вопросительного знака")

        return title
