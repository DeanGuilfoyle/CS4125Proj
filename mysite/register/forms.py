from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        #fields = ["first_name", "last_name", "email", "password1", "password2"]
        #fields = ["email", "password1", "password2"]
        fields = ["username", "password1", "password2"]
