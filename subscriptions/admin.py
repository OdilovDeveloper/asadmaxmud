from django.contrib import admin
from .models import SubscriptionLink

@admin.register(SubscriptionLink)
class SubscriptionLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'platform', 'url', 'channel_username',)
    actions = ['delete_selected']  # Delete tugmasini ko‘rsatadi
