from django.db import models

class AdminContact(models.Model):
    telegram_id = models.CharField(max_length=64)
    username = models.CharField(max_length=64, help_text="Foydalanuvchilar ushbu username orqali admin bilan bog‘lanadi")

    def __str__(self):
        return f"Admin: @{self.username}"