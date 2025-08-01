from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from payment.views import PaymeCallBackAPIView, ClickWebhookAPIView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("payment/update/", PaymeCallBackAPIView.as_view()),
    path("payment/click/update/", ClickWebhookAPIView.as_view()),
    path("api/v1/", include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
