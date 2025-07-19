import requests
from users.models import UserModel
from order.models import PaymentSession, OrderModel, OrderItemModel
from order.utils import extract_city_name
from order.city_ids import CITY_NAME_TO_ID_LATIN

def get_bts_token():
    url = 'http://api.bts.uz:8080/index.php?r=v1/auth/get-token'
    payload = {
        "username": "609662790",
        "password": "asatillo",
        "inn": "609662790"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", {}).get("token")
    raise Exception("BTS token olishda xatolik")


def create_bts_order_from_user_id(user_id):
    user = UserModel.objects.get(user_id=user_id)
    
    # Faqat to‘langan payment session’lar
    payment_sessions = PaymentSession.objects.filter(user=user, is_paid=True, tracking_code__isnull=True)

    if not payment_sessions.exists():
        raise Exception("To‘lov qilingan buyurtmalar topilmadi")

    # Barcha orderlarni yig‘ish
    all_orders = OrderModel.objects.filter(payment_sessions__in=payment_sessions).distinct()

    if not all_orders.exists():
        raise Exception("Buyurtmalar topilmadi")

    # OrderItem’larni yig‘ish
    all_items = OrderItemModel.objects.filter(order__in=all_orders)

    if not all_items.exists():
        raise Exception("Buyurtma mahsulotlari yo‘q")

    token = get_bts_token()

    # 👇 1-chi order dan foydalanuvchi ma’lumotlarini olamiz
    order = all_orders.first()

    # 📦 Mahsulotlar
    post_types = []
    for item in all_items:
        post_types.append({
            "name": item.product.name,
            "code": f"{item.product.id}-{item.id}",
            "count": item.quantity,
            "cost": int(item.price),
        })

    city_name = extract_city_name(order.country, order.address)
    receiver_city_id = CITY_NAME_TO_ID_LATIN.get(city_name)

    payload = {
        "clientId": f"user-{user.user_id}",
        "wcs_code": f"user-{user.user_id}",
        "senderDelivery": 1,
        "senderCityId": 25,  
        "senderAddress": "Andijon shahri",
        "senderReal": "Mamatqulov Asatillo",
        "senderPhone": "+998330060129",
        "weight": 2,
        "packageId": 4,
        "postTypeId": 16,
        "postTypes": post_types,
        "receiverDelivery": 1,
        "receiver": order.name,
        "receiverCityId": receiver_city_id,  
        "receiverAddress": order.address,
        "receiverPhone": order.phone,
        "piece": 1,
        "takePhoto": 1,
        'is_test': 1,
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post("http://api.bts.uz:8080/index.php?r=v1/order/add", json=payload, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"BTSga yuborishda xatolik: {response.text}")

    data = response.json()
    tracking_link = data.get("tracking")

    # tracking_code ni barcha sessionlarga yozamiz
    for ps in payment_sessions:
        ps.tracking_code = tracking_link
        ps.save()

    return tracking_link
