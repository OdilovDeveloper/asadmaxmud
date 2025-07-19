from django.contrib import admin, messages
from ..models import UserModel
from bts.services import create_bts_order_from_user_id
from unfold.admin import ModelAdmin as UnfoldModelAdmin 


@admin.register(UserModel)
class UserAdmin(UnfoldModelAdmin):
    list_display = (
        'id',
        "user_id",
        "__str__",
    )
    actions = ['generate_bts_tracking_link']

    @admin.action(description="📦 BTS tracking link yaratish")
    def generate_bts_tracking_link(self, request, queryset):
        for user in queryset:
            try:
                link = create_bts_order_from_user_id(str(user.user_id))
                self.message_user(
                    request,
                    f"✅ {user.name} uchun BTS tracking link: {link}",
                    level=messages.SUCCESS
                )
            except Exception as e:
                self.message_user(
                    request,
                    f"❌ {user.name} uchun xatolik: {e}",
                    level=messages.ERROR
                )
