from django.conf import settings
from django.db import models
from PIL import Image


class Ticket(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)

    IMAGE_MAX_SIZE = (800,800)

    def resize_image(self):
        """resize images in 800x800"""
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self) -> str:
        return f'{self.title}'