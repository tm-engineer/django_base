"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from utils.common import load_env


env = load_env()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('SETTINGS_MODULE'))

application = get_wsgi_application()
