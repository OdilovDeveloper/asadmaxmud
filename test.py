import os
import django

# ⚠️ Bu joyni loyihangga qarab to‘g‘rila
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  
django.setup()

from bts.services import create_bts_order_from_user_id

link = create_bts_order_from_user_id("8148586285")
print("✅ BTS tracking link:", link)