from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from waitapp import consumers,routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        routing.websocket_urlpatterns
    )
})
