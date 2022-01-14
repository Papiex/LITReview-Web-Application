from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class LoginForm(forms.Form):
    """Login form"""
    username = forms.CharField(max_length=63, label="Nom d'Utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")

class SignupForm(UserCreationForm):
    """Registration form"""
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)