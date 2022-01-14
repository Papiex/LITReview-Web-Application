from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """redirect to home.html"""
    return render(request, 'review/home.html')
