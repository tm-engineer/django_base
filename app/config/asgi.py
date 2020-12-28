"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from utils.common import load_env


env = load_env()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('SETTINGS_MODULE'))

application = get_asgi_application()
