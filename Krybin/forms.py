from django import forms
from .models import boxText


class boxTextForm(forms.ModelForm):
    class Meta:
        model = boxText
        fields = ['text']