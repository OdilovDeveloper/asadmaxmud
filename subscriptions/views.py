# subscriptions/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SubscriptionLink
from .serializers import SubscriptionLinkSerializer

class SubscriptionLinkListAPIView(APIView):
    def get(self, request):
        links = SubscriptionLink.objects.all()
        serializer = SubscriptionLinkSerializer(links, many=True)
        return Response(serializer.data)