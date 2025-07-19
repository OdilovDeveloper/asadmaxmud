from rest_framework import serializers
from .models import CaseLink

class CaseLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseLink
        fields = '__all__'