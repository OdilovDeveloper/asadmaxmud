from rest_framework import serializers
from .models import SiteSettings, FooterText

class SiteSettingsSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = SiteSettings
        fields = ['logo']

    def get_logo(self, obj):
        if obj.logo:
            return obj.logo.url.replace("http://", "https://")
        return None

class SiteFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterText
        fields = ['footer_text']