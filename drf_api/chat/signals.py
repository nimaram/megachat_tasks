from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Message

@receiver(post_save, sender=Message)
def broadcast_message(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        room_group_name = f"chat_{instance.conversation.id}"

        html_message = render_to_string('chat/partials/message_bubble.html', {'message': instance})

        async_to_sync(channel_layer.group_send)(
            room_group_name,
            {
                "type": "chat_message_html",
                "html": html_message
            }
        )