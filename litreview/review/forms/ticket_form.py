from django import forms
from ..models.ticket import Ticket

class TicketForm(forms.ModelForm):
    """Ticket form"""
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {'title': 'Titre'}

class DeleteTicketForm(forms.Form):
    """Delete ticket form"""
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)