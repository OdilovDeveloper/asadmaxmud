from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.models import UserModel
from order.models import PaymentSession


@api_view(['GET'])
def get_tracking_link(request):
    telegram_id = request.GET.get('telegram_id')

    if not telegram_id:
        return Response({'error': 'telegram_id kiritilmagan'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = UserModel.objects.get(user_id=telegram_id)
    except UserModel.DoesNotExist:
        return Response({'error': 'Bunday foydalanuvchi topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    # Eng so‘nggi to‘langan va tracking_code mavjud buyurtmani olish
    payment_session = PaymentSession.objects.filter(
        user=user,
        is_paid=True,
        tracking_code__isnull=False
    ).order_by('-created_at').first()

    if not payment_session:
        return Response({'error': 'Tracking link topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'tracking_link': payment_session.tracking_code
    }, status=status.HTTP_200_OK)
