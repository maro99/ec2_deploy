from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.1.1',
    '.amazonaws.com',
]

# Static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
MEDIA_ROOT = os.path.join(EC2_DEPLOY,'.media')
MEDIA_URL ='/media/'

# wsgi
WSGI_APPLICATION = 'config.wsgi.application'

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
