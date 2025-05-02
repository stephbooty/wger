"""
WSGI config for workout_manager project.
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Point to the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wger.extras.docker.production.settings')

# Standard Django WSGI app
application = get_wsgi_application()

# WhiteNoise handles static files
application = WhiteNoise(application, root='/opt/render/project/src/wger/staticfiles', prefix='static/')
