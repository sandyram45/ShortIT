from django import forms
from .models import urlEntry


class shortenerForm(forms.Form):
    url_field = forms.URLField(label='URL')


class url_shortenerForm(forms.ModelForm):
    class Meta:
        model = urlEntry
        fields = ['url']