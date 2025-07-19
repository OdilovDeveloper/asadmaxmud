from django.contrib import admin
from .models import LiveLink

@admin.register(LiveLink)
class LiveLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'link']