from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from . import forms


def login_page(request):
    """login form"""
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})

def logout_user(request):
    """Redirect to login.html"""
    logout(request)
    return redirect('login')

def signup_page(request):
    """Registration Form signup.html"""
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})