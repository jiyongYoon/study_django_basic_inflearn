"""
WSGI config for first_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_django.settings') # 운영 모드에서 사용하는 settings 파일설정. 개발 모드는 manage.py

application = get_wsgi_application()
