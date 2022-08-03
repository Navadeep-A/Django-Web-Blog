from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import profile

class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = User 
        #saves to User model
        fields = ['username','email','password1','password2']
        #  displays the order of the formelements

class UserUpdationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdationForm(forms.ModelForm):
    
    class Meta:
        model = profile
        fields = ['profile_image']
    
