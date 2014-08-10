__author__ = 'abhishekanurag'
from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=1)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())