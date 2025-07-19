import requests
from django.db import models
from django.conf import settings
from users.models import UserModel


class SendSMSModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    message = models.TextField(verbose_name="SMS matni")
    is_sent = models.BooleanField(default=False, verbose_name="Yuborildi")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Bitta foydalanuvchiga SMS"
        verbose_name_plural = "Bitta foydalanuvchiga SMSlar"

    def __str__(self):
        return f"SMS to {self.user.name}"

    def send_sms(self):
        # + belgisi bo‘lsa olib tashlash
        phone = self.user.phone.replace("+", "") if self.user.phone else ""
        url = "https://api.smsfly.uz/send"
        data = {
            "key": settings.SMSFLY_API_KEY, 
            "phone": phone,
            "message": self.message
        }
        response = requests.post(url, json=data)
        result = response.json()
        return result


class FreeSMSModel(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Telefon raqam")
    message = models.TextField(verbose_name="Xabar matni")
    is_sent = models.BooleanField(default=False, verbose_name="Yuborilganmi")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Erkin SMS yuborish"
        verbose_name_plural = "Erkin SMSlar"

    def __str__(self):
        return f"{self.phone} ga yuborilgan"

    def clean_phone(self):
        # Har doim 998 bilan boshlanadigan format
        phone = self.phone.replace("+", "").replace(" ", "").strip()
        if phone.startswith("998"):
            return phone
        elif phone.startswith("9") and len(phone) == 9:
            return "998" + phone
        elif phone.startswith("0") and len(phone) == 10:
            return "998" + phone[1:]
        return phone

    def send_sms(self):
        phone = self.clean_phone()
        url = "https://api.smsfly.uz/send"
        data = {
            "key": settings.SMSFLY_API_KEY,
            "phone": phone,
            "message": self.message
        }
        response = requests.post(url, json=data)
        return response.json()

    def save(self, *args, **kwargs):
        self.phone = self.clean_phone()
        super().save(*args, **kwargs)
