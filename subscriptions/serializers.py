# subscriptions/serializers.py
from rest_framework import serializers
from .models import SubscriptionLink

class SubscriptionLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionLink
        fields = ['id', 'name', 'platform', 'url', 'channel_username']
