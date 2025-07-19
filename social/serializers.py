# social/serializers.py
from rest_framework import serializers
from .models import SocialMedia

class SocialMediaSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = SocialMedia
        fields = ['id', 'name', 'icon', 'link']

    def get_icon(self, obj):
        return obj.icon.url.replace('http://', 'https://') if obj.icon else None
