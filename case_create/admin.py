from django.contrib import admin
from .models import CaseLink

@admin.register(CaseLink)
class CaseLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link')
    actions = ['delete_selected']  # Delete tugmasini ko‘rsatadi