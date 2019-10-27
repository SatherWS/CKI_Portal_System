from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalog.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required')
    university = forms.CharField(max_length=50, required=True, help_text='Required')
    password2 = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 
        'university','email', 'password1',)


