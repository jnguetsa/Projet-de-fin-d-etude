from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User= get_user_model()
from django import forms
#from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control col-10 w-4 ml-5', 'placeholder': "Entrer votre nom d'utilisateur"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control col-10 w-4  ml-5 ', 'placeholder': 'Entrez votre mot de passe'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control col-10  w-4  ml-5', 'placeholder': 'Confirmez votre mot de passe'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

