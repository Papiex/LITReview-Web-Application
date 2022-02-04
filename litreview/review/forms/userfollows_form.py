from django import forms
from ..models.userfollows import UserFollows

class UserFollowsForm(forms.Form):
    """UserFollows form"""
    class Meta:
        model = UserFollows
        fields = ['user', 'followed_user']