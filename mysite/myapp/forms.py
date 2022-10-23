# forms.py
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
  
    class Meta:
        model = Image
        fields = ['name', 'img']
    
class ImageForm2(forms.ModelForm):
  
    class Meta:
        model = Image
        fields = ['name', 'img']