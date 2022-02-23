from random import choices
from django.db import models
from django.conf import settings
from . import ticket


class Review(models.Model):

    STATUS = (
        ('&#9733;&#9734;&#9734;&#9734;&#9734;', ('1')),
        ('&#9733;&#9733;&#9734;&#9734;&#9734;', ('2')),
        ('&#9733;&#9733;&#9733;&#9734;&#9734;', ('3')),
        ('&#9733;&#9733;&#9733;&#9733;&#9734;', ('4')),
        ('&#9733;&#9733;&#9733;&#9733;&#9733;', ('5')),
    )

    ticket = models.ForeignKey(to=ticket.Ticket, on_delete=models.CASCADE)
    rating = models.CharField(choices=STATUS, max_length=128, default=1)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.headline}'
