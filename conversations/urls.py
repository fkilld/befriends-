from django.urls import path
from .views import *

app_name='conversations'

urlpatterns = [
    path('inbox/',inbox,name="inbox"),
    path('inbox/<int:profile_friend>', inbox, name="inbox_new_chat"),
    path('chatbox/<int:chat_id>', chatbox, name="chatbox"),
    path('delete/chat/<int:chat_id>', delete_chat, name="delete_chat"),
    path('delete/mesage/<int:message_id>', delete_message, name="delete_message"),

]
