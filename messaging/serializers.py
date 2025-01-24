from rest_framework import serializers
from .models import Message ,User

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['id', 'timestamp']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class InboxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ["sender", "content", "timestamp"]
