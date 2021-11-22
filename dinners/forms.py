from django import forms
from .models import Dinner

class DinnerForm(forms.ModelForm):
    class Meta:
        model = Dinner
        fields = [
            'title',
            'description',
            #'time',
            'place'
        ]    