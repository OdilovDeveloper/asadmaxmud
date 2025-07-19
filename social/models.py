# social/models.py
from django.db import models
from cloudinary.models import CloudinaryField

class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    icon = CloudinaryField('icon')  # Cloudinary rasm
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar"
