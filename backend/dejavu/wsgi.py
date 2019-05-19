import os
import sys

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'dejavu.settings.production')

path = '/opt/django/dejavu'
if path not in sys.path:
    sys.path.insert(0, path)

application = get_wsgi_application()
