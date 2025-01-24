from rest_framework import serializers
from .models import Message ,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class InboxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ["sender", "content", "timestamp"]
