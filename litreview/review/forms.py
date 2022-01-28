from django import forms
from . import models

class TicketForm(forms.ModelForm):
    """Ticket form"""
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        labels = {'title': 'Titre'}

class DeleteTicketForm(forms.Form):
    """Delete ticket form"""
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class ReviewForm(forms.ModelForm):
    """Review Form"""
    class Meta:
        model = models.Review
        fields = ['headline','rating', 'body']
        labels = {'headline': 'Titre', 'rating': 'Note', 'body': 'Commentaire'}