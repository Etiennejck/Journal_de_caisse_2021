"""
ASGI config for Journal_de_caisse_2021 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Journal_de_caisse_2021.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application()
})

