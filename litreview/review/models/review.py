from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from . import ticket


class Review(models.Model):
    ticket = models.ForeignKey(to=ticket.Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.headline}'