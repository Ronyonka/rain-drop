from django import forms
from .models import *


class RainForm(forms.ModelForm):
    class Meta:
        model = Rain
        fields = ['date', 'amount']

