from django import forms
from django.contrib.auth.models import User
from .models import Phone
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PhoneForm(forms.Form):
    number = forms.CharField(max_length=12)


class CodeForm(forms.Form):
    code = forms.CharField(max_length=6)
