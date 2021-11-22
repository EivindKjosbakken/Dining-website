from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import OwnUser
from .models import User


class SignUpForm(forms.ModelForm):

   class Meta:
       model = User
       fields = [
           'username',
           'password',
           'age',
           'address',
           'allergies',

       ] #Fjernet 'name'

class LoginForm(forms.ModelForm):

    class Meta:
        model = OwnUser
        fields = [
            'username',
            'password'
        ]
