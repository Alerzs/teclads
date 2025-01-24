from rest_framework.views import APIView
from rest_framework import generics
from .serializers import UserSerializer ,InboxSerializer
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Message
from django.contrib.auth.models import User
from .tasks import send_message


class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        sender = request.user
        reciever_username = request.data.get('reciever')
        content = request.data.get('content')

        if not reciever_username or not content:
            return Response({'error': 'Receiver and content are required.'}, status=status.HTTP_400_BAD_REQUEST)

        task = send_message.delay(sender.id, reciever_username, content)
        return Response({'status': f'Message queued successfully id = {task.id}'}, status=status.HTTP_200_OK)


class InboxView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InboxSerializer

    def get_queryset(self):
        return Message.objects.filter(reciever=self.request.user)
  


    


