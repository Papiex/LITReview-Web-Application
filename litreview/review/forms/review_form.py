from django import forms
from ..models.review import Review


class ReviewForm(forms.ModelForm):
    """Review Form"""
    class Meta:
        model = Review
        fields = ['headline','rating', 'body']
        labels = {'headline': 'Titre', 'rating': 'Note', 'body': 'Commentaire'}

class DeleteReviewForm(forms.Form):
    """Delete ticket form"""
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)