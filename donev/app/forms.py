from django import forms
from .models import Donor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth import password_validation 

class LoginForm(AuthenticationForm):
    username = UsernameField(required=True,widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control','placeholder':'Username'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs=
    {'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs=
    {'class':'form-control','placeholder':'Enter Password Again'}))

    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email ID'}),
            

        }