from django.urls import path
from .views import MessageView, Login, Register, InboxView

urlpatterns = [
    path('login/', Login.as_view(), name='Login'),
    path('register/', Register.as_view(), name='Register'),
    path('messages/', InboxView.as_view(), name='Inbox'),
    path('messages/send/', MessageView.as_view(), name='Compose'),

]
