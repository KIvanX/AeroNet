import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.template.defaulttags import url
from authorization.consumer import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AeroNet.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'ws/$', ChatConsumer.as_asgi()),
        ])
    ),
})

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             re_path(r"^front(end)/$", consumers.AsyncChatConsumer.as_asgi()),
#         ])
#     ),
# })