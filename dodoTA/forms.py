from dataclasses import field

from django import forms

from . import models

class form1(forms.ModelForm):
    class Meta:
        model=models.havijpolomorgh
        fields='__all__'
