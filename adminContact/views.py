from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AdminContact

@api_view(["GET"])
def get_admin_contact(request):
    admin = AdminContact.objects.last()
    if admin:
        return Response({
            "username": admin.username,
            "link": f"https://t.me/{admin.username}"
        })
    return Response({"error": "Admin ma'lumotlari topilmadi"}, status=404)