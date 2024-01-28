from django import forms
from .models import CustomUser
from .validators import *


class Patient(forms.ModelForm):
    username = forms.CharField(
            max_length = 20,
            unique = True,
            validators = [username_validators]
        )
    password = forms.CharField(
            max_length = 50,
            unique = False,
            validators = [password_validators]
        )
    email = forms.EmailField(
            max_length = 254,
            blank = True,
            null = True
        )
    date_joined = forms.DateTimeField(
            auto_now_add=True
        )
    last_login = forms.DateTimeField(
            auto_now=True
        )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'date_joined', 'last_login']
        
class Secretary(forms.ModelForm):
    username = forms.CharField(
            max_length = 20,
            unique = True,
            validators = [username_validators]
        )
    password = forms.CharField(
            max_length = 50,
            unique = False,
            validators = [password_validators]
        )
    email = forms.EmailField(
            max_length = 254,
            blank = True,
            null = True
        )
    date_joined = forms.DateTimeField(
            auto_now_add=True
        )
    last_login = forms.DateTimeField(
            auto_now=True
        )

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'date_joined', 'last_login']
