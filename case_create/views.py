from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CaseLink
from .serializers import CaseLinkSerializer

class CaseLinkAPIView(APIView):
    def get(self, request):
        link = CaseLink.objects.last()  # eng oxirgi link
        if link:
            serializer = CaseLinkSerializer(link)
            return Response(serializer.data)
        return Response({"detail": "Link topilmadi."}, status=404)