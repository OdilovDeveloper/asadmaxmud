from django.contrib import admin
from .models import SocialMedia

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link',)
    actions = ['delete_selected']  # Delete tugmasini ko‘rsatadi
