from rest_framework.views import APIView
from rest_framework.response import Response
from logo.models import SiteSettings, FooterText
from logo.serializers import SiteSettingsSerializer, SiteFooterSerializer

class SiteSettingsView(APIView):
    def get(self, request):
        obj = SiteSettings.objects.last()
        serializer = SiteSettingsSerializer(obj)
        return Response(serializer.data)


class FooterAPIView(APIView):
    def get(self, request):
        setting = FooterText.objects.last()
        serializer = SiteFooterSerializer(setting)
        return Response(serializer.data)