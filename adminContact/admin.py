from django.contrib import admin
from .models import AdminContact

@admin.register(AdminContact)
class AdminContactAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username')
    actions = ['delete_selected']