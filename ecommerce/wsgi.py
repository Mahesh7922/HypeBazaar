"""WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use DJANGO_SETTINGS_MODULE environment variable if set, otherwise use default
settings_module = os.environ.get("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
