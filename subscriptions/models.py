# subscriptions/models.py
from django.db import models

class SubscriptionLink(models.Model):
    PLATFORM_CHOICES = [
        ('telegram', 'Telegram'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
    ]

    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    channel_username = models.CharField(max_length=100, blank=True, null=True)  # faqat Telegram uchun

    def __str__(self):
        return f"{self.name} ({self.platform})"

    class Meta:
        verbose_name = "Obuna link"
        verbose_name_plural = "Obuna linklari"
