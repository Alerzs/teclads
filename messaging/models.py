from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    sender = models.ForeignKey(User ,related_name="sender" , on_delete=models.SET_NULL, null=True)
    reciever = models.ForeignKey(User ,related_name="reciever", on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

