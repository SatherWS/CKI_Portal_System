from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalog.models import User,Club_Chapter, Service_Project
from django.db import models

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required')
    chapter =  models.ForeignKey('Club_Chapter',on_delete=models.PROTECT)
    password2 = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 
        'chapter','email', 'password1',)
