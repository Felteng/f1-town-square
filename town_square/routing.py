from django.urls import path, include
from town_square.consumers import ChatConsumer


# Source: https://www.geeksforgeeks.org/realtime-chat-app-using-django/

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]
