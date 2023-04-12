from django.db import models


class ChatMessage(models.Model):
    chat_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    fle_id = models.CharField(max_length=100)
    is_fle = models.BooleanField(default=False)
    message = models.CharField(max_length=1000)
    prompt = models.CharField(max_length=500, null=True)
    is_true_prompt = models.BooleanField(default=False)
    is_last_message = models.BooleanField(default=False)
    chat_duration = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} | {}".format(self.chat_id, self.user_id)
