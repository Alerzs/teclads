from celery import shared_task
from .models import Message
from django.contrib.auth.models import User

@shared_task
def send_message(sender_id, reciever_username, content):
    try:
        sender = User.objects.get(id=sender_id)
        reciever = User.objects.get(username=reciever_username)

        Message.objects.create(sender=sender, reciever=reciever, content=content)
        return f"Message from {sender.username} to {reciever.username} created successfully."
    except User.DoesNotExist as e:
        return f"Failed to create message: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


