from tkinter.messagebox import NO
from django import forms
from ..models.review import Review

class ReviewForm(forms.ModelForm):
    """Review Form"""
    NOTES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rating = forms.ChoiceField(widget=forms.RadioSelect(), choices=NOTES)


    class Meta:
        model = Review
        fields = ['headline','rating', 'body']
        labels = {'headline': 'Titre', 'rating': 'Note', 'body': 'Commentaire'}


class DeleteReviewForm(forms.Form):
    """Delete ticket form"""
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)