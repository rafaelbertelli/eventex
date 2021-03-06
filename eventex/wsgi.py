"""
WSGI config for eventex project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventex.settings')

application = Cling(get_wsgi_application())
