from django.urls import path
from . import views

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("start/<int:user_id>/", views.start_chat, name="start_chat"),
    path("chat/<int:conversation_id>/", views.chat_detail, name="chat_detail"),
    path("chat/<int:conversation_id>/send/", views.send_message, name="send_message"),
]
