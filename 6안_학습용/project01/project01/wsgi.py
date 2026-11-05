# 공부 지도: learning/files/project01/wsgi.py.md
# 역할: Django 실행 설정과 전체 주소 연결
"""
WSGI config for project01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project01.settings')

application = get_wsgi_application()
