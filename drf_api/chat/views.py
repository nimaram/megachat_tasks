from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Conversation, Message


@login_required
def inbox(request):
    conversations = request.user.conversations.all().order_by("-updated_at")

    # Add other_user for each conversation
    conversations_with_other_user = []
    for convo in conversations:
        other_user = convo.get_other_user(request.user)
        conversations_with_other_user.append(
            {"conversation": convo, "other_user": other_user}
        )

    users = User.objects.exclude(id=request.user.id)

    return render(
        request,
        "chat/inbox.html",
        {
            "conversations_with_other_user": conversations_with_other_user,
            "users": users,
        },
    )


@login_required
def start_chat(request, user_id):
    target_user = get_object_or_404(User, id=user_id)

    conversations = Conversation.objects.filter(participants=request.user).filter(
        participants=target_user
    )

    if conversations.exists():
        conversation = conversations.first()
    else:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, target_user)

    return redirect("chat_detail", conversation_id=conversation.id)


@login_required
def chat_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)

    if request.user not in conversation.participants.all():
        return HttpResponseForbidden("You are not in this chat")

    messages = conversation.messages.all()

    return render(
        request,
        "chat/chat_detail.html",
        {
            "conversation": conversation,
            "messages": messages,
            "other_user": conversation.get_other_user(request.user),
        },
    )


@login_required
def send_message(request, conversation_id):
    if request.method == "POST":
        conversation = get_object_or_404(Conversation, id=conversation_id)
        content = request.POST.get("content")

        if content:
            message = Message.objects.create(
                conversation=conversation, sender=request.user, content=content
            )
            conversation.save()

            # Return the message HTML to append immediately for the sender
            # WebSocket will broadcast to other participants
            from django.template.loader import render_to_string
            
            # Return message HTML with out-of-band input clear
            message_html = render_to_string('chat/partials/message_bubble.html', {'message': message, 'user': request.user}, request=request)
            
            # Return combined response - message will append to #chat-messages, input will clear via oob
            return render(request, 'chat/partials/message_with_input_clear.html', {
                'message_html': message_html
            })

    return HttpResponseForbidden()
