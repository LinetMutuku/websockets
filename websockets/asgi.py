import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from app.consumers import Consumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websockets.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            Consumer.as_asgi()
        ),
    }
)