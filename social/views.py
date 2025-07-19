from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SocialMedia
from .serializers import SocialMediaSerializer

class SocialMediaListAPIView(APIView):
    def get(self, request):
        queryset = SocialMedia.objects.all()
        serializer = SocialMediaSerializer(queryset, many=True)
        return Response(serializer.data)
