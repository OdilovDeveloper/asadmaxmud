from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views.product import ProductViewSet, ProductDetailView, CategoryView, BannerView
from users.views.users import UserView
from order.views.order import OrderView, UserOrdersView
from basket.views.basket import GetBasketView, BasketView
from bot.views import AboutView, AdvertisingView
from services.views import PaymentCreate, ClickCreate
from logo.views import SiteSettingsView, FooterAPIView
from social.views import SocialMediaListAPIView
from subscriptions.views import SubscriptionLinkListAPIView
from adminContact.views import get_admin_contact
from case_create.views import CaseLinkAPIView
from bts.views import get_tracking_link
from live.views import LiveLinkView
from second_webapp.views import ProductListAPIView
router = DefaultRouter()

# product urls
router.register(r'products', ProductViewSet, basename='product')
router.register(r"product_detail", ProductDetailView, basename='product_detail')
router.register(r'cart/(?P<user_id>\d+)', GetBasketView, basename='t')

# category urls
router.register(r"category", CategoryView, basename='category')

# users urls
router.register(r"users", UserView, basename='users')

# add urls
router.register(r"cart", BasketView, basename='cart')
router.register(r"banner", BannerView, basename='banner')
router.register(r"about", AboutView, basename='about')
router.register(r"advertising", AdvertisingView, basename='advertising')

urlpatterns = [
    path("", include(router.urls)),
    path("order/", OrderView.as_view(), name='order'),
    path("order/<int:user_id>/", UserOrdersView.as_view(), name='getusers'),
    path('payment/create/', PaymentCreate.as_view(), name='payment_create'),
    path('payment/click/create/', ClickCreate.as_view(), name='click_create'),
    path('settings/', SiteSettingsView.as_view()),
    path('social/', SocialMediaListAPIView.as_view()),
    path('subscribe/', SubscriptionLinkListAPIView.as_view()),
    path('footer/text/', FooterAPIView.as_view(), name='site-settings'),
    path('admin/link/', get_admin_contact),
    path('case/link/', CaseLinkAPIView.as_view(), name='case-link'),
    path('get-tracking-link/', get_tracking_link, name='get-tracking-link'),
    path('live/', LiveLinkView.as_view(), name='live-link'),
    path('productlist/', ProductListAPIView.as_view(), name='product-list'),
]