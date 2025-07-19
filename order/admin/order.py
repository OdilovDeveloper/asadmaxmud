from django.contrib import admin
from ..models import OrderModel, OrderItemModel, PaymentSession
from unfold.admin import ModelAdmin as UnfoldModelAdmin

@admin.register(OrderItemModel)
class OrderItemAdmin(UnfoldModelAdmin):
    """
    Admin Interface for OrderItem
    """
    list_display = (
        "id",
        "order",
        "product",
        "quantity",
        "price",
        "created_at",
    )
    search_fields = ('id', )


class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    extra = 1


@admin.register(OrderModel)
class OrderAdmin(UnfoldModelAdmin):
    """
    Admin Interface for Order
    """
    list_display = (
        "id",
        "name",
        "phone",
        "is_paid",
        "payment_method",
        "delivery_type",
        "created_at",
    )
    list_filter = ('is_paid', 'payment_method', 'delivery_type')
    search_fields = ('id', 'name', 'phone')
    inlines = [OrderItemInline]


@admin.register(PaymentSession)
class PaymentSessionAdmin(UnfoldModelAdmin):
    """
    Admin Interface for PaymentSession
    """
    list_display = (
        "id",
        "user",
        "total_amount",
        "is_paid",
        "tracking_code",  # ✅ qo‘shildi
        "created_at",
    )
    list_filter = ("is_paid", "created_at")
    search_fields = ("id", "user__name", "user__user_id", "payme_transaction_id", "tracking_code")
    readonly_fields = ("created_at", "tracking_code")  # ✅ tracking_code ni faqat o‘qish uchun

    filter_horizontal = ("orders",)
