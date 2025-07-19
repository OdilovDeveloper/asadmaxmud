from django.contrib import admin
from .models import SiteSettings, FooterText

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('logo',)
    actions = ['delete_selected']  # Delete tugmasini ko‘rsatadi

@admin.register(FooterText)
class Footer_textAdmin(admin.ModelAdmin):
    list_display = ("id", "footer_text",)
    actions = ['delete_selected']