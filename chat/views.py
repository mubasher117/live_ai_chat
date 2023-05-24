from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import ChatMessage
from django.utils import timezone

from utility.prompts import prompts


class ChatViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        is_true_prompt = True
        is_fle = data.get("is_fle", False)
        message_number = data.get("message_number", 1)
        prompt = prompts[message_number % len(prompts)] if not is_fle else None
        chat_id=data.get("chat_id")
        last_message = ChatMessage.objects.filter(chat_id=chat_id).last()
        last_message_duration = None
        if last_message:
            chat_duration = timezone.now() - timezone.localtime(last_message.created_at)
            last_message_duration = chat_duration.total_seconds()
        user_id = data.get("user_id", None)
        fle_id = data.get("fle_id", None)
        ChatMessage.objects.create(
            chat_id=chat_id,
            chat_name=user_id+"_"+fle_id,
            user_id=user_id,
            fle_id=fle_id,
            is_fle=is_fle,
            message=data.get("message", None),
            prompt=prompt,
            is_true_prompt=is_true_prompt,
            last_message_duration=last_message_duration
        )
        response = {"prompt": prompt}
        return Response(data=response, status=status.HTTP_200_OK)

    @action(detail=False, methods=["POST"])
    def end_chat(self, request, *args, **kwargs):
        data = request.data
        messages = ChatMessage.objects.filter(chat_id=data.get("chat_id"))
        first_message = messages.first()
        last_message = messages.last()
        last_message.is_last_message = True
        current_time = timezone.now()
        chat_duration = current_time - timezone.localtime(first_message.created_at)
        last_message.chat_duration = chat_duration.total_seconds()
        last_message.save()

        response = {
            "message": "Chat Ended Successfully!",
            "chat_id": first_message.chat_id,
        }
        return Response(data=response, status=status.HTTP_200_OK)
