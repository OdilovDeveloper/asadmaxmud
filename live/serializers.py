from rest_framework import serializers
from .models import LiveLink

class LiveLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveLink
        fields = ['id', 'link']