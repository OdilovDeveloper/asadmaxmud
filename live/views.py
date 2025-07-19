from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LiveLink
from .serializers import LiveLinkSerializer

class LiveLinkView(APIView):
    def get(self, request):
        try:
            link = LiveLink.objects.last()
            serializer = LiveLinkSerializer(link)
            return Response(serializer.data)
        except LiveLink.DoesNotExist:
            return Response({'link': None})
