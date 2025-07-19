from django.contrib import admin, messages
from .models import SendSMSModel, FreeSMSModel


@admin.register(SendSMSModel)
class SendSMSAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "is_sent", "created_at")
    readonly_fields = ("is_sent", "created_at")

    def save_model(self, request, obj, form, change):
        result = obj.send_sms()

        if result.get("success"):
            obj.is_sent = True
            self.message_user(request, "SMS muvaffaqiyatli yuborildi.", messages.SUCCESS)
        else:
            self.message_user(request, f"Xatolik: {result.get('reason')}", messages.ERROR)

        super().save_model(request, obj, form, change)

@admin.register(FreeSMSModel)
class FreeSMSAdmin(admin.ModelAdmin):
    list_display = ("phone", "message", "is_sent", "created_at")
    readonly_fields = ("is_sent", "created_at")

    def save_model(self, request, obj, form, change):
        result = obj.send_sms()

        if result.get("success"):
            obj.is_sent = True
            self.message_user(request, f"{obj.phone} raqamga SMS yuborildi.", messages.SUCCESS)
        else:
            self.message_user(request, f"Xatolik: {result.get('reason')}", messages.ERROR)

        super().save_model(request, obj, form, change)