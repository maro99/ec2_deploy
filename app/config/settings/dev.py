from .base import *

DEBUG = True


# Static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
EC2_DEPLOY = os.path.dirname(BASE_DIR)
MEDIA_ROOT = os.path.join(EC2_DEPLOY,'.media')
MEDIA_URL ='/media/'

# wsgi
WSGI_APPLICATION = 'config.wsgi.application'

# DB
SECRET_DIR =os.path.join(EC2_DEPLOY,'.secrets')
json_data = open(f'{SECRET_DIR}/dev.json').read()
data = json.loads(json_data)
DATABASES = data["DATABASES"]