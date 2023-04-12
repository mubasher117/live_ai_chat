from django.contrib import admin
from .models import ChatMessage


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "user_id", "fle_id", "is_true_prompt")
    list_filter = ("user_id", "fle_id", "chat_id")
    search_fields = ("user_id", "fle_id", "chat_id")


admin.site.register(ChatMessage, ChatMessageAdmin)
